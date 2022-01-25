
# 自我對弈模組
from game import State
from pv_mcts import pv_mcts_scores
from dual_network import DN_OUTPUT_SIZE
from datetime import datetime
from tensorflow.keras.models import load_model
from tensorflow.keras import backend as K
from pathlib import Path
import numpy as np
import pickle
import os

# 設定參數
SP_GAME_COUNT = 10 # 進行自我對弈的遊戲局數（原版為25000）
SP_TEMPERATURE = 1.0 # 波茲曼分布的溫度參數

# 計算先手的局勢價值
def first_player_value(ended_state):
    if ended_state.is_lose():
        return -1 if ended_state.is_first_player() else 1
    return 0

# 儲存訓練資料
def write_data(history):
    now = datetime.now()
    os.makedirs('./data/', exist_ok=True)
    path = './data/{:04}{:02}{:02}{:02}{:02}{:02}.history'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    with open(path, mode='wb') as f:
        pickle.dump(history, f)

# 進行 1 次完整對戰
def play(model):
    history = []

    state = State()#產生新對局

    while True:
        if state.is_done():#遊戲結束
            break

        scores = pv_mcts_scores(model, state, SP_TEMPERATURE)#取得合法棋步

        policies = [0] * DN_OUTPUT_SIZE #DN_OUTPUT_SIZE=7表示可動作的地方(每一回合只有7個位置可下棋)
        for action, policy in zip(state.legal_actions(), scores):
            policies[action] = policy #取得策略
        history.append([[state.pieces, state.enemy_pieces], policies, None])#在history增加敵我棋子配置、策略

        action = np.random.choice(state.legal_actions(), p=scores)#依照scores去選擇下一步

        state = state.next(action)#下棋並取得當前局勢

    # 在訓練資料中增加價值
    value = first_player_value(state)#取得局勢價值
    for i in range(len(history)):
        history[i][2] = value#根據history的每一步添加先手價值 
        value = -value #加負號為後手價值
    return history

# 自我對弈
def self_play():
    history = []

    # 載入最佳玩家的模型
    model = load_model('./model/best.h5')#載入最佳玩家模型

    for i in range(SP_GAME_COUNT):#以指定的次數進行遊戲
        h = play(model) #進行1次遊戲
        history.extend(h) #完整對戰資料存入history

        # 輸出
        print('\rSelfPlay {}/{}'.format(i+1, SP_GAME_COUNT), end='')
    print('')

    # 儲存訓練資料
    write_data(history)

    K.clear_session()#呼叫後端刪除模型
    del model

