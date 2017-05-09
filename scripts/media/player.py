# ! /usr/bin/python3
from threading import Thread
import subprocess
import time


class Player(Thread):
    """
    A class which display videos
    @Djavan Sergent
    """

    def __init__(self, video, rec, params):
        Thread.__init__(self)
        self.par = params
        self.video = video
        self.recorder = rec

    def run(self):
        if self.par.env != "prod":
            print("start playing")

        subprocess.call([self.par.media_player_path, self.video, '--play-and-exit', '--qt-video-autoresize'])

        if self.par.env != "prod":
            print("end playing")
        time.sleep(1)
        self.recorder.end = True  # Stop the record
