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
        self.video_path = "../../data/vid_show/"  # video to show
        self.record_path = "../../data/vid_usr/"  # face record while showing videos
        self.audio_path = "../../data/audio/"  # audio of videos
        self.eval_path = "../../data/evals/"  # evaluations of videos
        if platform.system() == "Windows":
            self.cmd_vlc = "./vlc/vlc.exe"
        else:
            self.cmd_vlc = "vlc"

    def set_user(self, user_id):
        self.user = user_id