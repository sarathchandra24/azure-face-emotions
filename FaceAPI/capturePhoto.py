import random
import cv2 as cv
import matplotlib.pyplot as plt
import time


def main():
    cap = cv.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    random_number = random.randint(0, 10000000)
    image = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    print(image)
    plt.imshow(image)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    # image = cv.imwrite(".images/"+str(random_number) + '.jpg', frame)
    image = cv.imwrite("images/hi.jpg", frame)
    cap.release()


def capture():
    cap = cv.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    random_number = random.randint(0, 10000000)
    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    image_name="ton1"+str(random_number)+".jpg"
    cv.imwrite(image_name, frame)
    # print(image)
    # plt.imshow(image)
    # plt.title('Color Image RGB')
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()
    cap.release()
    time.sleep(5)
    return image_name

if __name__ == "__main__":
    main()