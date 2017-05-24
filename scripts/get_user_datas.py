# ! /usr/bin/python3
# @Djavan Sergent
from random import shuffle
from function import check_dir, list, check_vlc
from interface.views import EvalView, RecapView, IdView, TrueFalseView
from media.evaluator import Evaluator, Evaluation
from media.params import Params
from media.player import Player
from media.recorder import Recorder

if __name__ == "__main__":

    # Parameters
    par = Params(env="dev")
    ev = Evaluator(params=par)

    # Test if directory exists
    check_vlc(par)
    check_dir(par.video_path)
    check_dir(par.record_path)
    check_dir(par.eval_path)

    # List of medias to play
    videos = list(par.video_path)
    fams = list(par.video_path+'fam/')

    if len(videos) == 0:
        print("unable to find video in directory " + par.video_path)
    else:
        # user id (training version only)
        main_view = IdView(par)
        main_view.create()
        main_view.show()

        # user directory
        usr_dir = par.record_path + par.user + '/'
        check_dir(usr_dir)

        # familiarisation
        fam_ev = Evaluator(par)
        for fam in fams:
            in_path = par.video_path + 'fam/' + fam
            media_player = Player(video=in_path, rec=Recorder(output="", params=par), params=par)
            media_player.start()
            media_player.join()

            # FunnyOrNot interface
            fam_eva = Evaluation(fam_ev)
            funny_view = TrueFalseView(params=par, evaluation=fam_eva)
            funny_view.create()
            funny_view.show()

            # Evaluation interface
            eval_view = EvalView(video=fam, params=par, evaluation=fam_eva)
            eval_view.create()
            eval_view.show()

        # for each video, we play it and record the user face
        shuffle(videos)  # random order
        for video in videos:
            # files to use
            in_path = par.video_path + video
            out_path = usr_dir + video

            # threads
            face_recorder = Recorder(output=out_path, params=par)
            media_player = Player(video=in_path, rec=face_recorder, params=par)

            # start the threads and run methods
            media_player.start()
            face_recorder.start()

            # wait for all threads to sync
            media_player.join()
            face_recorder.join()

            # evaluation tools
            eva = Evaluation(ev)
            funny_view = TrueFalseView(params=par, evaluation=eva)
            funny_view.create()
            funny_view.show()
            eval_view = EvalView(video=video, params=par, evaluation=eva)
            eval_view.create()
            eval_view.show()

        ev.write()
        title = "Récapitulatif : " + par.user
        recap_view = RecapView(params=par, evaluator=ev, title=title)
        recap_view.create()
        recap_view.show()
