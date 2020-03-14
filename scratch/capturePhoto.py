import cv2 as cv
import time


def capture(name):
    cap = cv.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image_name = str(name) + ".jpg"
    cv.imwrite(image_name, frame)
    cap.release()
    time.sleep(0)
    return image_name


if __name__ == "__main__":
    name = capture("sar123")
    print("name is", name)
