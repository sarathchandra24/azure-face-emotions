import cv2 as cv
# import required.show_image as si


def capture(name):
    cap = cv.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    # If there is a need to show the image then un-comment the below line
    # si.image_show(image)

    image_name = str(name)
    cv.imwrite(image_name,frame)
    cap.release()

    # time.sleep(0)

    return image_name


if __name__ == "__main__":
    capture("img1.jpg")
