import tkinter as tk
from PIL import Image, ImageTk


class Interface():

    def __init__(self, title="MakeMeLaught", bg="#FFFFFF", sizex=400, sizey=100):
        self.window = tk.Tk()
        self.title = title
        self.background = bg
        self.size_x = sizex
        self.size_y = sizey
        self.ctrl_frame = tk.Frame(self.window, width=self.size_x, height=self.size_y)

    def create(self):
        self.window.wm_title(self.title)
        self.window.config(background=self.background)
        btn_next = tk.Button(self.window, text="Ok", command=self.cmd_next)
        slider = tk.Scale(self.window, from_=0, to=10, length=400, tickinterval=1, orient=tk.HORIZONTAL)
        slider.pack()
        btn_next.pack()

    def cmd_next(self):
        print("next")

    def cmd_play(self):
        print("play")

    def show(self):
        self.window.mainloop()
