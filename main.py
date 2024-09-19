import numpy as np
from PIL import Image

dark_image = Image.open("test/darkpage.png")
bkground_image = Image.open("test/bkgnd.png")


def negative(dark_image):
    ngative_dark_image_array = 255 - np.array(dark_image)
    negative_image = Image.fromarray(ngative_dark_image_array)
    return negative_image.show()


def shading_correction(dark_image):
    shading_func = np.array(bkground_image)/255
    estimated_image_array = np.array(dark_image) / shading_func
    estimated_image = Image.fromarray(estimated_image_array)
    threshold = 200
    estimated_image_array[estimated_image_array < threshold] = 0
    estimated_image_array[estimated_image_array > threshold] = 255
    new_image = Image.fromarray(estimated_image_array)
    return estimated_image.show(), new_image.show()



def binarizing(dark_image):
    grey_darkimage = dark_image.convert()
    grey_darkimage_array = np.array(grey_darkimage)
    grey_bkgdimage = bkground_image.convert()
    grey_bkgdimag_array = np.array(grey_bkgdimage)
    new_image_array = (grey_bkgdimag_array - grey_darkimage_array)
    threshold = 150
    new_image_array[new_image_array < threshold] = 0
    new_image_array[new_image_array > threshold] = 255
    new_image = Image.fromarray(new_image_array)
    return new_image.show(), print(new_image_array)



dark_image.show()
bkground_image.show()
negative(dark_image)
shading_correction(dark_image)
binarizing(dark_image)
