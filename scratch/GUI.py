import tkinter
from tkinter import *

import PIL.Image, PIL.ImageTk
import cv2
import face_API.face_analyze as FA


def open_window():
    top = Toplevel()
    top.title("Validation Window")
    top.geometry("300x300+120+120")
    button1 = Button(top, text="close")
    button1.pack()
    top.after(3000, lambda: top.destroy())


class App:

    def validate(self):
        self.take_snapShot()

    def __init__(self, videoSource=0):
        self.root = tkinter.Tk()
        self.root.title("Validation of a person")
        self.videoSource = videoSource

        # display the video in the pane
        self.video = VideoCapture(self.videoSource)
        self.canvas = tkinter.Canvas(self.root, width=self.video.width, height=self.video.height)
        self.canvas.pack()

        # crate a button for validating the pic
        self.valid_button = tkinter.Button(self.root, text="Authenticate", command=self.validate())
        self.valid_button.pack(anchor=tkinter.CENTER, expand=TRUE)

        self.delay = 15
        self.update()

        self.root.mainloop()


    def take_snapShot(self):
        ret, frame = self.video.get_frame()
        if ret:
            print("came here")
            cv2.imwrite("frame-read.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

            # FA.face_analyze("frame-read")

    def update(self):
        ret, frame = self.video.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.root.after(self.delay, self.update)


class VideoCapture:

    def __init__(self, videoSource):
        self.root = Tk()
        self.vid = cv2.VideoCapture(videoSource)

        # verifying if the video cam is available or not
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", videoSource)

        # setting the size of pane to the video cam
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


App()
