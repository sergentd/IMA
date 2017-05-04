# ! /usr/bin/python3
# @Djavan Sergent
from os.path import exists

from pygame import mixer
from recorder import Recorder

from function import check_dir, list, afpath
from player import Player

if __name__ == "__main__":

    mixer.init()

    # media paths
    video_path = "../data/videos/show/"  # video to show
    record_path = "../data/videos/record/"  # face record while showing videos
    audio_path = "../data/audio/"  # audio of videos

    # Test if directory exists
    check_dir(video_path)
    check_dir(record_path)

    # List of medias to play
    videos = list(video_path)

    if len(videos) == 0:
        print("unable to find video in directory " + video_path)
    else:

        # user id (training version only)
        userid = input("N° utilisateur : ")

        # for each video, we play it and record the user face
        for video in videos:
            # files to use
            in_path = video_path + video
            out_path = record_path + userid + "_" + video
            audio_file = audio_path + afpath(video)

            # threads
            face_recorder = Recorder(out_path)
            media_player = Player(in_path, face_recorder)
            if exists(audio_file):
                mixer.music.load(audio_file)

            # start the threads and run methods
            media_player.start()
            face_recorder.start()
            if exists(audio_file):
                mixer.music.play()

            # wait for all threads to sync
            media_player.join()
            face_recorder.join()
            if exists(audio_file):
                mixer.music.stop()
