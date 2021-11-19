from PIL import Image
import numpy as np


def do_filter(count_gradations, mosaic_size):
    img = Image.open("img2.jpg")
    array = np.array(img)
    size_img = array.shape

    for i in range(0, size_img[0], mosaic_size):
        for j in range(0, size_img[1], mosaic_size):
            paint_cell(array, i, j, mosaic_size, count_gradations)

    res = Image.fromarray(array)
    res.save('res.jpg')


def find_average_brightness(arr, px_width, px_height, mosaic):
    return np.average(arr[px_width: px_width + mosaic, px_height: px_height + mosaic])


def paint_cell(arr, width, height, mosaic_size, count_gradations):
    gradations = 255 // count_gradations
    average_brightness = find_average_brightness(arr, width, height, mosaic_size)
    arr[width: width + mosaic_size, height: height + mosaic_size] = average_brightness // gradations * gradations


do_filter(100, 20)
