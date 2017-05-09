#! /usr/bin/python3
# @Djavan Sergent
from os import listdir, makedirs
from os.path import isfile, join, exists, basename, splitext
from interface import ChooseMediaPlayerView


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
