# ! /usr/bin/python3
# @Djavan Sergent
from player import Player
from recorder import Recorder
from function import check_dir, list

if __name__ == "__main__":

    # media paths
    video_path = "../data/videos/show/"
    record_path = "../data/videos/record/"

    # Test if directory exists
    check_dir(video_path)
    check_dir(record_path)

    # List of medias to play
    videos = list(video_path)

    if len(videos) == 0:
        print("unable to find video in directory " + video_path)
    else:

        # user id (training version only)
        id = input("N° utilisateur : ")

        # for each video, we play it and record the user face
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
