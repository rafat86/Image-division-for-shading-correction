
# Machine Vision
# Assignment 01
# Ra'fat Naserdeen


import numpy as np
from PIL import Image

dark_image = Image.open("darkpage.png").convert('L')
bkground_image = Image.open("bkgnd.png").convert('L')


def negative(image):
    ngative_dark_image_array = 255 - np.array(image)
    negative_image = Image.fromarray(ngative_dark_image_array)
    return negative_image.show()


def shading_binary(image):
    shading_func = np.array(bkground_image)/255
    estimated_image_array = np.array(image) / shading_func
    estimated_image = Image.fromarray(estimated_image_array)
    threshold = 200
    estimated_image_array[estimated_image_array < threshold] = 0
    estimated_image_array[estimated_image_array > threshold] = 255
    new_image = Image.fromarray(estimated_image_array)
    return estimated_image.show(), new_image.show()


dark_image.show()
bkground_image.show()
negative(dark_image)
shading_binary(dark_image)
