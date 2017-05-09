#! /usr/bin/python3
"""
    @ Djavan Sergent
    Interfaces of the application.
    - EvalView : display evaluation tools (slider)
    - RecapView : display a recapitulation of evaluations
    - DistractView : display a distraction task
"""
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


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
        btn_next = tk.Button(self.window, text="Ok", command=self.cmd_eval, width=30)
        self.slider = tk.Scale(self.window, from_=0, to=10, length=self.size_x, tickinterval=1, orient=tk.HORIZONTAL)
        self.slider.grid(row=0, columnspan=20)

        # Images
        img_neutre = Image.open("../../ressources/img/neutre.png")
        img_sourire = Image.open("../../ressources/img/sourire.png")
        img_rire = Image.open("../../ressources/img/rire.png")

        # TK compatible
        tk_neutre = ImageTk.PhotoImage(img_neutre)
        tk_sourire = ImageTk.PhotoImage(img_sourire)
        tk_rire = ImageTk.PhotoImage(img_rire)

        # Label
        lb_neutre = tk.Label(image=tk_neutre)
        lb_neutre.image = tk_neutre
        lb_sourire = tk.Label(image=tk_sourire)
        lb_sourire.image = tk_sourire
        lb_rire = tk.Label(image=tk_rire)
        lb_rire.image = tk_rire
        lb_neutre.grid(row=1, column=0, columnspan=2)
        lb_sourire.grid(row=1, column=10, columnspan=2)
        lb_rire.grid(row=1, column=19, columnspan=2)

        btn_next.grid(row=2, column=10, columnspan=2)
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


class ChooseMediaPlayerView:
    """
    A class which display distraction task
    """

    def __init__(self, params, title="MakeMeLaught", bg="#FFFFFF", sizex=100, sizey=40):
        self.window = tk.Tk()
        self.par = params
        self.title = title
        self.background = bg
        self.size_x = sizex
        self.size_y = sizey
        self.path = ""

    def create(self):
        self.window.wm_title(self.title)
        self.window.config(background=self.background)
        self.window.attributes("-topmost", True)
        btn_next = tk.Button(self.window, text="Select VLC directory", command=self.cmd_choose, width=30)
        btn_next.pack()

    def cmd_choose(self):
        self.par.media_player_path = filedialog.askopenfilename()
        print("Média player : ", self.par.media_player_path)
        self.close()

    def show(self):
        self.create()
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
