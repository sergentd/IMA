#! /usr/bin/python3
"""
    @ Djavan Sergent
    Interfaces of the application.
    - EvalView : display evaluation tools (slider)
    - RecapView : display a recapitulation of evaluations
    - DistractView : display a distraction task
"""
import tkinter as tk


class EvalView:
    """
    A class which display evaluation tools
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
        btn_next = tk.Button(self.window, text="Ok", command=self.cmd_eval)
        self.slider = tk.Scale(self.window, from_=0, to=10, length=self.size_x, tickinterval=1, orient=tk.HORIZONTAL)
        self.slider.pack()
        btn_next.pack()
        self.window.attributes("-topmost", True)

    def cmd_eval(self):
        evaluation = self.par.user + ";" + self.video + ";" + str(self.slider.get())
        self.ev.add(evaluation)
        if self.par.env != "prod":
            print("evaluation saved")
        self.close()

    def show(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
        self.window.destroy()


class RecapView:
    """
    A class which display recapitulation
    """

    def __init__(self, params, evaluator, title="MakeMeLaught", bg="#FFFFFF", sizex=400, sizey=400):
        self.window = tk.Tk()
        self.par = params
        self.ev = evaluator
        self.title = title
        self.background = bg
        self.size_x = sizex
        self.size_y = sizey
        pass

    def create(self):
        self.window.wm_title(self.title)
        self.window.config(background=self.background)
        self.window.attributes("-topmost", True)
        pass

    def cmd_recap(self):
        self.close()

    def show(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
        self.window.destroy()


class DistractView:
    """
    A class which display distraction task
    """

    def __init__(self, params, title="MakeMeLaught", bg="#FFFFFF", sizex=400, sizey=400):
        self.window = tk.Tk()
        self.par = params
        self.title = title
        self.background = bg
        self.size_x = sizex
        self.size_y = sizey

    def create(self):
        self.window.wm_title(self.title)
        self.window.config(background=self.background)
        self.window.attributes("-topmost", True)

    def cmd_task(self):
        self.close()

    def show(self):
        self.window.mainloop()

    def close(self):
        self.window.quit()
        self.window.destroy()
