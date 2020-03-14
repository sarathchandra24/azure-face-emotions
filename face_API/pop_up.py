# import tkinter as t
#
# class Ap:
#     def __init__(self,image_name):
#         self.root1=t.Tk()
#         self.root1.title("Face image")
#         _image = t.PhotoImage(file=image_name)
#         labe = t.LabelFrame(image=_image)
#         labe.pack()
#
#         self.root1.after(3000,lambda: self.root1.destroy())
#         self.root1.mainloop()
#
#
# if __name__ == '__main__':
#     Ap("sar123.jpg")
#
import tkinter as tk

from PIL import ImageTk

canvas_width = 500
canvas_height = 500


class Ton:
    def __init__(self, image_name):
        master = tk.Tk()
        canvas = tk.Canvas(master,
                           width=canvas_width,
                           height=canvas_height)
        canvas.pack()

        img = ImageTk.PhotoImage(file=image_name)
        canvas.create_image(10, 10, anchor=tk.NW, image=img)
        master.mainloop()


if __name__ == '__main__':
    image_name = "sar123.jpg"
    Ton(image_name)
