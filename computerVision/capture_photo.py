import cv2 as cv


# import matplotlib.pyplot as plt

# for testing uncomment the matplotlib import to see your image

def main():
    cap = cv.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    # print("Frame")
    # print(frame)
    img1 = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    imageto = cv.imwrite('images/HI' + '.jpg', frame)

    # plt.imshow(img1)
    # plt.title('Color Image RGB')
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()

    cap.release()


if __name__ == "__main__":
    main()


def capture_photo():
    cap = cv.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    img1 = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    imageto = cv.imwrite('ToGetAttributes' + str(0) + '.jpg', frame)
    cap.release()
    return img1
