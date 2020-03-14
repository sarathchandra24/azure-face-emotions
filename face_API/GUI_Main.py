import tkinter
from tkinter import *
import random as rand
import PIL.Image as PI
import cv2
import time
from PIL import ImageTk
import face_API.face_analyze as fa
import face_API.showImage as si

video_Source = 0



class App():
    def __init__(self):
        self.root = Tk()
        self.root.title("Eidiko Validation")
        self.Video_Frame = Frame(self.root, width=500, height=500)
        self.Video_Frame.pack(side=LEFT, fill=BOTH, expand=TRUE)

        self.video = VideoCapture(video_Source)

        self.canvas = Canvas(self.Video_Frame, width=self.video.width, height=self.video.height)
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=TRUE)

        self.Validate_Frame = Frame(self.root, width=500, height=500)
        self.Validate_Frame.pack(side=RIGHT)

        img = ImageTk.PhotoImage(PI.open("empty.jpg"))
        self.panel = Label(self.Validate_Frame, image=img)
        self.panel.pack(side="bottom", fill="both", expand="yes")

        self.Button = Button(self.Validate_Frame, text="Authenticate", command=self.snapshot)
        self.Button.pack(anchor=tkinter.CENTER, expand=TRUE)

        self.delay = 50
        self.update()
        self.root.mainloop()

    def update(self):
        ret, frame = self.video.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=PI.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.root.after(self.delay, self.update)

    def snapshot(self):
        random_Nam = rand.randint(0, 200)
        temp, frame = self.video.get_frame()
        image_file_name = "C:/Users/Sarat/PycharmProjects/AzureFaceEmotions/face_API/temp_images/temp"+str(random_Nam) + ".jpg"
        cv2.imwrite(image_file_name, frame)
        fa.face_analyze(image_file_name)
        # print("file name is ", image_file_name)
        self.panel.configure(image=image_file_name)
        # si.image_show(image=image_file_name)
        pass


class VideoCapture:

    def __init__(self, videoSource):
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


if __name__ == '__main__':
    App()
