#! /usr/bin/python3
# @Djavan Sergent
# Extract audio (wav) files from avi files using ffmpeg
import subprocess
from os.path import basename, splitext, abspath

from function import check_dir, list
from params import Params

par = Params()
check_dir(par.audio_path)
files = list(par.video_path)

for f in files:
    output = splitext(basename(f))[0]
    path = par.video_path + f
    print(path)
    outpath = abspath(par.audio_path) + "\\" + output + ".wav"
    command = "D:/ffmpeg.exe -i " + path + " -ab 160k -ac 2 -ar 44100 -vn " + outpath
    subprocess.call(command, shell=True)