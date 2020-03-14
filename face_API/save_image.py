import matplotlib.pyplot as plt


def image_show(image):
    # print(image)
    plt.imshow(image)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()