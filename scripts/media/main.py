# ! /usr/bin/python3
# @Djavan Sergent
# from os.path import exists
# import database.dbmanager as db
from evaluator import Evaluator
from function import check_dir, list, afpath
from player import Player
# from pygame import mixer
from recorder import Recorder
from interface import EvalView
from params import Params

if __name__ == "__main__":

    # Database init
    # db.Base.metadata.create_all(db.engine)

    # Création de l'instance de l'ORM
    # session = db.Session()

    # session.commit()

    # Parameters
    par = Params(env="dev")
    ev = Evaluator(params=par)

    # Audio mixer init
    # mixer.init()

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
        if par.env != "prod":
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
            # audio_file = par.audio_path + afpath(video)

            # Evaluation interface
            window = EvalView(video=video, params=par, evaluator=ev)
            window.create()

            # threads
            face_recorder = Recorder(output=out_path, params=par)
            media_player = Player(video=in_path, rec=face_recorder, params=par)
            # if exists(audio_file):
            #   mixer.music.load(audio_file)

            # start the threads and run methods
            # if exists(audio_file):
            #     mixer.music.play()
            media_player.start()
            face_recorder.start()

            # wait for all threads to sync
            media_player.join()
            face_recorder.join()
            # if exists(audio_file):
            #     mixer.music.stop()

            # evaluation tools
            window.show()
        ev.write()