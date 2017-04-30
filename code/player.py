# ! /usr/bin/python3
import numpy as np
from threading import Thread
import time
import cv2


class Player(Thread):
    """
    A class which display vidéo
    @Djavan Sergent
    """

    def __init__(self, video, rec):
        Thread.__init__(self)
        self.video = video
        self.recorder = rec

    def run(self):
        print("Start playing")
        cap = cv2.VideoCapture(self.video)

        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(50) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        print("end playing")
        cv2.destroyAllWindows()
        time.sleep(2)  # Capture 2 seconds after the video end
        self.recorder.end = True  # Stop the record
