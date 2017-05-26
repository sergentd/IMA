# ! /usr/bin/python3
from threading import Thread
import cv2


class Recorder(Thread):
    """
    A class which capture videos of user's face
    @Djavan Sergent
    """

    def __init__(self, output, params):
        Thread.__init__(self)
        self.par = params
        self.output = output
        self.end = False

    def run(self):
        cap = cv2.VideoCapture(0)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(self.output, fourcc, 20.0, (640, 480))
        if self.par.env != "prod":
            print("start record...")
        while (cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                out.write(frame)
                if self.end:
                    break
            else:
                break
        # Release everything if job is finished
        cap.release()
        out.release()
        if self.par.env != "prod":
            print("record stoped")
            print("record saved")
        cv2.destroyAllWindows()