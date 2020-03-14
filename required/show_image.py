import cv2
import numpy as np
from matplotlib import pyplot as plt


def image_show(image):
    img = cv2.imread("../face_API/temp_images"+image, 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

# image_show("sar123.jpg")