#! /usr/bin/python3
# @Djavan Sergent
# Extract audio (wav) files from avi files using ffmpeg
import subprocess
from function import check_dir, list
from os.path import basename, splitext, abspath

audio_path = "../data/audio/"
video_path = "../data/videos/show/"
check_dir(audio_path)
files = list(video_path)

for f in files:
    output = splitext(basename(f))[0]
    path = video_path + f
    print(path)
    outpath = abspath(audio_path) + "\\" + output + ".wav"
    command = "D:/ffmpeg.exe -i " + path + " -ab 160k -ac 2 -ar 44100 -vn " + outpath
    subprocess.call(command, shell=True)