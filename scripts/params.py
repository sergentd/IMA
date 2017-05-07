#! /usr/bin/python3


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
        self.eval_path = "../../data/vid_eval/"  # audio of videos

    def set_user(self, user_id):
        self.user = user_id