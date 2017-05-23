#! /usr/bin/python3
# @Djavan Sergent
from os import listdir, makedirs
from os.path import isfile, join, exists, basename, splitext
from interface.views import ChooseMediaPlayerView


# check the existence of a directory
def check_dir(dir):
    if not exists(dir):
        makedirs(dir)


# check the existance of vlc program
def check_vlc(par):
    if not exists(par.media_player_path):
        cvmp = ChooseMediaPlayerView(params=par)
        cvmp.show()


# list of files in a directory
def list(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]


def afpath(video):
    return splitext(basename(video))[0] + ".wav"


def center(window):
    w = window.winfo_width()
    h = window.winfo_height()

    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


def get_filename(file):
    return splitext(basename(file))[0]
