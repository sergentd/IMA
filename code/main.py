# ! /usr/bin/python3
from player import Player
from recorder import Recorder
from os import listdir
from os.path import isfile, join


if __name__ == "__main__":

    video_path = "./videos/show/"
    record_path = "./videos/record/"

    videos = [f for f in listdir(video_path) if isfile(join(video_path, f))]

    id = input("N° utilisateur : ")

    for video in videos:
        # files to use
        in_path = video_path + video
        out_path = record_path + id + "_" + video

        # threads
        face_recorder = Recorder(out_path)
        media_player = Player(in_path, face_recorder)

        # start the threads and run methods
        media_player.start()
        face_recorder.start()

        # wait for all threads to sync
        media_player.join()
        face_recorder.join()
