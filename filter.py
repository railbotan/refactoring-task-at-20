from PIL import Image
import numpy as np


def apply_filter(mosaic_size, count_gradations):
    img = Image.open("img2.jpg")
    arr = np.array(img)
    len_width = len(arr)
    len_height = len(arr[1])

    px_width = 0
    while px_width < len_width - mosaic_size - 1:
        px_height = 0
        while px_height < len_height - mosaic_size - 1:
            average_brightness = find_average_brightness_cell(arr, px_width, px_height, mosaic_size)
            paint_cell(arr, px_width, px_height, mosaic_size, average_brightness, count_gradations)
            px_height = px_height + mosaic_size
        px_width = px_width + mosaic_size
    res = Image.fromarray(arr)
    res.save('res.jpg')


def find_average_brightness_cell(arr, px_width, px_height, mosaic_size):
    sum_brightness = 0
    for i in range(px_width, px_width + mosaic_size):
        for j in range(px_height, px_height + mosaic_size):
            r = arr[i][j][0]
            g = arr[i][j][1]
            b = arr[i][j][2]
            median = r // 3 + g // 3 + b // 3
            sum_brightness += median
    average_brightness = sum_brightness // mosaic_size ** 2
    return average_brightness


def paint_cell(arr, px_width, px_height, mosaic_size, average_brightness, count_gradations):
    for i in range(px_width, px_width + mosaic_size):
        for j in range(px_height, px_height + mosaic_size):
            gradations = 255 // count_gradations
            arr[i][j][0] = average_brightness // gradations * gradations
            arr[i][j][1] = average_brightness // gradations * gradations
            arr[i][j][2] = average_brightness // gradations * gradations

