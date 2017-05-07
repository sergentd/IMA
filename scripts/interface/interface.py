#! /usr/bin/python3
import tkinter as tk


class Interface:
    """
    A class which display evaluation tools
    @Djavan Sergent
    """

    def __init__(self, video, params, evaluator, title="MakeMeLaught", bg="#FFFFFF", sizex=400, sizey=100):
        self.window = tk.Tk()
        self.par = params
        self.title = title
        self.background = bg
        self.size_x = sizex
        self.size_y = sizey
        self.video = video
        self.ev = evaluator

    def create(self):
        self.window.wm_title(self.title)
        self.window.config(background=self.background)
        self.btn_next = tk.Button(self.window, text="Ok", command=self.cmd_eval)
        self.slider = tk.Scale(self.window, from_=0, to=10, length=self.size_x, tickinterval=1, orient=tk.HORIZONTAL)
        self.slider.pack()
        self.btn_next.pack()

    def cmd_eval(self):
        evaluation = self.par.user + ";" + self.video + ";" + str(self.slider.get())
        self.ev.add(evaluation)
        self.window.quit()
        self.window.destroy()

    def show(self):
        self.window.mainloop()
