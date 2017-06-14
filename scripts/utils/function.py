#! /usr/bin/python3
# @Djavan Sergent
from os import listdir, makedirs
from os.path import isfile, join, exists, basename, splitext
from interface.views import ChooseMediaPlayerView
from matplotlib import pyplot as plt


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


# filename without extension
def get_filename(file):
    return splitext(basename(file))[0]


# Plot the dummy analyse
def plot(name, label, res, au, auv):
    # Plot title
    plt.suptitle(name + " > " + 'Classe : ' + label + ' | Prediction : ' + res)
    # Subplot 1 : AU presence
    # plt.subplot(211)
    plt.ylabel("Presence")
    plt.xlabel("frame")
    for e in au:
        plt.plot(e)
    # Subplot 2 : AU intensity
    # plt.subplot(212)
    # plt.ylabel("intensity")
    # plt.xlabel("frame")
    # for e in auv:
    #     plt.plot(e)

    plt.show()
