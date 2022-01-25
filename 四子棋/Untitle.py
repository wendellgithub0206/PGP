import tkinter as tk
from tkinter.constants import RIGHT
import tkinter.messagebox
from tkinter.messagebox import askokcancel, showinfo

from game import State
from pv_mcts import pv_mcts_action
from tensorflow.keras.models import load_model
from pathlib import Path
from threading import Thread
import tkinter as tk

# 載入最佳玩家模型
model = load_model('./model/best.h5')
class SampleApp(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
class StartPage(tk.Frame):
    def __init__(self, master):
        def confirm_to_lt():
            if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
                self.quit()
        tk.Frame.__init__(self, master)
        self.master.title('四子棋')
        startbt = tk.Button(self, text='開始遊戲', bg='orange', fg='black', font=('Arial', 18),command=lambda: master.switch_frame(gameStart))
        startbt['width'] = 30
        startbt['height'] = 4
        startbt['activebackground'] = 'blue'  
        startbt['activeforeground'] = 'black' 
        startbt.pack(side='top',ipady=5, pady=100,padx=80)
        lt = tk.Button(self, text='退出', bg='red', fg='black', font=('Arial', 18),command=confirm_to_lt)
        lt['width'] = 20
        lt['height'] = 2
        lt['activebackground'] = 'blue'  
        lt['activeforeground'] = 'black' 
        lt.pack(side='top',padx=80)
        c = tk.Canvas(self, width = 500, height = 100,highlightthickness = 0)
        c.pack()



class gameStart(tk.Frame):
    def __init__(self, master=None, model=model):
        tk.Frame.__init__(self, master)
        self.master.title('四子棋')

        self.state = State()

        self.next_action = pv_mcts_action(model, 0.0)

        # 產生新的畫布元件
        self.c = tk.Canvas(self, width = 840, height = 720, highlightthickness = 0)
        self.c.bind('<Button-1>', self.turn_of_human)
        self.c.pack()

        # 更新盤面的UI
        self.on_draw()

    # 輪到人類下棋
    def turn_of_human(self, event):
        # Step01 判斷遊戲是否結束
        if self.state.is_done():
            if self.state.is_lose():
                ms =tkinter.messagebox.askokcancel('温馨提示', '你輸了! 按確定重新開始,取消退出遊戲') 
                if ms==True:
                    showinfo(title='温馨提示',message='已重新開始')
                elif ms==False:
                    self.quit()
            self.state = State()
            self.on_draw()
            return

        # Step02 判斷是否輪到人類下棋
        if not self.state.is_first_player():
            return

        # Step03 將滑鼠點擊的位置轉換成「下棋」的動作
        x = int(event.x/120)
        if x < 0 or 6 < x:
            return
        action = x
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
            if self.state.is_lose():
                ms =tkinter.messagebox.askokcancel('温馨提示', '你贏了! 按確定重新開始,取消退出遊戲') 
                if ms==True:
                    showinfo(title='温馨提示',message='已重新開始')
                elif ms==False:
                    self.quit()
            self.state = State()
            self.on_draw()
            return

        # Step02 下子
        action = self.next_action(self.state)

        # Step03 取得下一個局勢 (盤面)
        self.state = self.state.next(action)
        self.on_draw()

    # 繪製棋子
    def draw_piece(self, index, first_player):
        x = (index%7)*120+15
        y = int(index/7)*120+15
        if first_player:
            self.c.create_oval(x, y, x+90, y+90, width = 1.0, fill = '#000000')
        else:
            self.c.create_oval(x, y, x+90, y+90, width = 1.0, fill = '#FFFFFF')

    # 繪製 UI3
    def on_draw(self):
        self.c.delete('all')
        self.c.create_rectangle(0, 0, 840, 720, width = 0.0, fill = '#888888')
        for i in range(42):
            x = (i%7)*120+15
            y = int(i/7)*120+15
            self.c.create_oval(x, y, x+90, y+90, width = 1.0, fill = '#BB5500')

        for i in range(42):
            if self.state.pieces[i] == 1:
                self.draw_piece(i, self.state.is_first_player())
            if self.state.enemy_pieces[i] == 1:
                self.draw_piece(i, not self.state.is_first_player())



if __name__ == "__main__":
    base = SampleApp()
    base.mainloop()
   