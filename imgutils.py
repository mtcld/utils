import cv2
import os
import matplotlib.pyplot as plt


def imlist(path):
    """
        list all the files in folder
    :param path:
    :return: list of files' path
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


def imshow(im_title, im):
    """
        Show an image
    :param im_title: title of image
    :param im: binary image
    :return: None
    """
    plt.figure()
    plt.title(im_title)
    plt.axis("off")

    if len(im.shape) == 2:
        plt.imshow(im, cmap="gray")
    else:
        im_display = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        plt.imshow(im_display)

    plt.show()


def imreads(path):
    """
        Read all img in a given folder
    :param path: path of folder
    :return: list of binary images
    """
    images_path = imlist(path)
    images = []
    for i in images_path:
        images.append(cv2.imread(i))
    return images



