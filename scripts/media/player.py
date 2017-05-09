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

    # def run(self):
    #     if self.par.env != "prod":
    #         print("start playing")
    #     cap = cv2.VideoCapture(self.video)
    #
    #     while (cap.isOpened()):
    #         ret, frame = cap.read()
    #         if ret:
    #             cv2.imshow('MakeMeLaught', frame)
    #             if cv2.waitKey(31) & 0xFF == ord('q'):
    #                 break
    #         else:
    #             break
    #
    #     cap.release()
    #     if self.par.env != "prod":
    #         print("end playing")
    #     cv2.destroyAllWindows()
    #     self.recorder.end = True  # Stop the record

    def run(self):
        if self.par.env != "prod":
            print("start playing")

        p = subprocess.call([self.par.media_player_path, self.video, '--play-and-exit', '--qt-video-autoresize'])

        if self.par.env != "prod":
            print("end playing")
        time.sleep(2)
        self.recorder.end = True  # Stop the record
