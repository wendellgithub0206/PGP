
# 五子棋

import random
import math
import tkinter.messagebox
# 遊戲局勢
class State:
    # 初使化
    def __init__(self, pieces=None, enemy_pieces=None):
        self.pieces = pieces if pieces != None else [0] * 81
        self.enemy_pieces = enemy_pieces if enemy_pieces != None else [0] * 81

    # 取得棋子數量
    def piece_count(self, pieces):
        count = 0
        for i in pieces:
            if i == 1:
                count +=  1
        return count

    # 判斷是否落敗
    def is_lose(self):
        # 判斷是否有五子連成一線
        def is_comp(x, y, dx, dy):
            for k in range(5):
                if y < 0 or 8 < y or x < 0 or 8 < x or self.enemy_pieces[x+y*9] == 0:
                    return False
                x, y = x+dx, y+dy
            return True

        # 判斷是否落敗
        for j in range(9):
            for i in range(9):
                if is_comp(i, j, 1, 0) or is_comp(i, j, 0, 1) or is_comp(i, j, 1, -1) or is_comp(i, j, 1, 1): #(i,j,1,0)判斷橫列(0,1)判斷直行(1,-1)判斷右上左下(1,1)判斷左上右下
                    return True
        return False

    # 判斷是否平手
    def is_draw(self):
        return self.piece_count(self.pieces) + self.piece_count(self.enemy_pieces) == 81 

    # 判斷遊戲是否結束
    def is_done(self):
        return self.is_lose() or self.is_draw()

    # 取得下一個局勢 (盤面)
    def next(self, action):
        pieces = self.pieces.copy()
        pieces[action]=1
        return State(self.enemy_pieces, pieces)

    # 取得合法棋步的串列
    def legal_actions(self):
        actions = []
        for i in range(81):
            if self.pieces[i] == 0 and self.enemy_pieces[i] == 0:
                actions.append(i)
        return actions

    # 判斷是否為先手
    def is_first_player(self):
        return self.piece_count(self.pieces) == self.piece_count(self.enemy_pieces)
    