# ! /usr/bin/python3
# @Djavan Sergent
from os.path import exists

from pygame import mixer
from recorder import Recorder
from function import check_dir, list, afpath
from player import Player
from params import Params
from evaluator import Evaluator
from interface.interface import Interface

if __name__ == "__main__":
    # Parameters
    par = Params(env="dev")
    ev = Evaluator(params=par)

    # Audio mixer init
    mixer.init()

    # Test if directory exists
    check_dir(par.video_path)
    check_dir(par.record_path)
    check_dir(par.eval_path)

    # List of medias to play
    videos = list(par.video_path)

    if len(videos) == 0:
        print("unable to find video in directory " + par.video_path)
    else:
        # user id (training version only)
        if par.env == ("dev" or "test"):
            par.set_user(input("ID utilisateur : "))
        else:
            userid = "0"

        usr_dir = par.record_path + par.user + '/'
        check_dir(usr_dir)

        # for each video, we play it and record the user face
        for video in videos:
            # files to use
            in_path = par.video_path + video
            out_path = usr_dir + video
            audio_file = par.audio_path + afpath(video)

            # Evaluation interface
            window = Interface(video=video, params=par, evaluator=ev)
            window.create()

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

            # evaluation tools
            window.show()
        ev.write()