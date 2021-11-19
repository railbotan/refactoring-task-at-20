from PIL import Image
import numpy as np


def apply_filter(mosaic_size, count_gradations):
    img = Image.open("img2.jpg")
    data_img = np.array(img)
    size_img = data_img.shape

    for x in range(0, size_img[0], mosaic_size):
        for y in range(0, size_img[1], mosaic_size):
            paint_cell(data_img, x, y, mosaic_size, count_gradations)

    res = Image.fromarray(data_img)
    res.save('res.jpg')


def find_average_brightness_cell(arr, px_width, px_height, mosaic_size):
    return np.average(arr[px_width:px_width + mosaic_size, px_height: px_height + mosaic_size])


def paint_cell(arr, px_width, px_height, mosaic_size, count_gradations):
    average_brightness = find_average_brightness_cell(arr, px_width, px_height, mosaic_size)
    gradations = 255 // count_gradations
    px_brightness = average_brightness // gradations * gradations
    arr[px_width:px_width + mosaic_size, px_height:px_height + mosaic_size, ][:] = px_brightness


apply_filter(10, 4)
