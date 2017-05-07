# ! /usr/bin/python3
import numpy as np
from threading import Thread
import cv2


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
        cap = cv2.VideoCapture(self.video)

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                cv2.imshow('MakeMeLaught', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        if self.par.env != "prod":
            print("end playing")
        cv2.destroyAllWindows()
        self.recorder.end = True  # Stop the record
