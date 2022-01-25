
# 人類與 AI 的對戰

from game import State
from pv_mcts import pv_mcts_action
from tensorflow.keras.models import load_model
from pathlib import Path
from threading import Thread
import tkinter as tk

# 載入最佳玩家模型
model = load_model('./model/best.h5')

# 初始化GameUI
class GameUI(tk.Frame):
    def __init__(self, master=None, model=None):
        tk.Frame.__init__(self, master)
        self.master.title('五子棋')

        self.state = State()

        self.next_action = pv_mcts_action(model, 0.0)

        # 產生新的畫布元件
        self.c = tk.Canvas(self, width = 800, height = 800, highlightthickness = 0)
        self.c.bind('<Button-1>', self.turn_of_human)
        self.c.pack()

        # 更新盤面的UI
        self.on_draw()

    # 輪到人類下棋
    def turn_of_human(self, event):
        # Step01 判斷遊戲是否結束
        if self.state.is_done():
            self.state = State()
            self.on_draw()
            return

        # Step02 判斷是否輪到人類下棋
        if not self.state.is_first_player():
            return

        # Step03 將滑鼠點擊的位置轉換成「下棋」的動作
        x = int((event.x-80)/80)
        y = int((event.y-80)/80)
        if x < 0 or  9< x or y < 0 or 9 < y:
            return
        action = x+y*9

        # Step04 判斷點擊的位置是否為合法棋步
        if not (action in self.state.legal_actions()):
            return

        # Step05 取得下一個局勢 (盤面)
        self.state = self.state.next(action)
        self.on_draw()

        # Step06 轉由 AI 進行下棋
        self.master.after(1, self.turn_of_ai)

    # 輪到 AI 下棋
    def turn_of_ai(self):
        # Step01 判斷遊戲是否結束
        if self.state.is_done():
            return

        # Step02 下子
        action = self.next_action(self.state)

        # Step03 取得下一個局勢 (盤面)
        self.state = self.state.next(action)
        self.on_draw()

    # 繪製棋子
    def draw_piece(self, index, first_player):
        x = (index%9)*80+80
        y = int(index/9)*80+80
        if first_player:
            self.c.create_oval(x-30, y-30, x+30, y+30, width = 1.0, fill = '#000000')
        else:
            self.c.create_oval(x-30, y-30, x+30, y+30, width = 1.0, fill = '#FFFFFF')

    # 繪製 UI
    def on_draw(self):
        self.c.delete('all')
        self.c.create_rectangle(0, 0, 800, 800, width = 0.0, fill = '#D26900')
        
        self.c.create_line(80, 80, 80, 720,  width = 2.0, fill = '#000000')
        self.c.create_line(720, 80, 720, 720,  width = 2.0, fill = '#000000')
        
        self.c.create_line(80, 80, 720, 80,  width = 2.0, fill = '#000000')
        self.c.create_line(80, 720, 720, 720,  width = 2.0, fill = '#000000')
        
        self.c.create_line(160, 80, 160, 720, width= 2.0, fill='#000000')
        self.c.create_line(240, 80, 240, 720, width= 2.0, fill='#000000')
        self.c.create_line(320, 80, 320, 720, width= 2.0, fill='#000000')
        self.c.create_line(400, 80, 400, 720, width= 2.0, fill='#000000')
        self.c.create_line(480, 80, 480, 720, width= 2.0, fill='#000000')
        self.c.create_line(560, 80, 560, 720, width= 2.0, fill='#000000')
        self.c.create_line(640, 80, 640, 720, width= 2.0, fill='#000000')
        
        self.c.create_line(80, 160, 720, 160, width= 2.0, fill='#000000')
        self.c.create_line(80, 240, 720, 240, width= 2.0, fill='#000000')
        self.c.create_line(80, 320, 720, 320, width= 2.0, fill='#000000')
        self.c.create_line(80, 400, 720, 400, width= 2.0, fill='#000000')
        self.c.create_line(80, 480, 720, 480, width= 2.0, fill='#000000')
        self.c.create_line(80, 560, 720, 560, width= 2.0, fill='#000000')
        self.c.create_line(80, 640, 720, 640, width= 2.0, fill='#000000')
        for i in range(81):
            if self.state.pieces[i] == 1:
                self.draw_piece(i, self.state.is_first_player())
            if self.state.enemy_pieces[i] == 1:
                self.draw_piece(i, not self.state.is_first_player())

# 顯示視窗
f = GameUI(model=model)
f.pack()
f.mainloop()