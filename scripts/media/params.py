#! /usr/bin/python3
import platform


class Params:
    """
    A simple class to store application parameters
    @Djavan Sergent
    """
    def __init__(self, env="dev"):
        self.name = "params"
        self.env = env
        self.user = ""
        self.video_path = "../data/vid_show/"  # video to show
        self.record_path = "../data/vid_usr/"  # face record while showing videos
        self.eval_path = "../data/evals/"  # evaluations of videos
        if platform.system() == "Windows":
            self.media_player_path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
        else:
            self.media_player_path = "/usr/bin/vlc"

    def set_user(self, user_id):
        self.user = user_id
