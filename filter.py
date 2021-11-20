from PIL import Image
import numpy as np


def mid_bright(arr, x, y, element_side):
    s = 0
    for row in range(x, x + element_side):
        for col in range(y, y + element_side):
            r = arr[row][col][0]
            g = arr[row][col][1]
            b = arr[row][col][2]
            s += int(r) + int(g) + int(b)

    midBright = int(s // (element_side * element_side))
    return midBright


def set_grey(arr, midBright, x, y, element_side, step):
    for row in range(x, x + element_side):
        for col in range(y, y + element_side):
            shade_of_grey = int(midBright // step) * step / 3
            arr[row][col][0] = shade_of_grey
            arr[row][col][1] = shade_of_grey
            arr[row][col][2] = shade_of_grey


def transform_img(image_file, element_side, gradation):
    img = Image.open(image_file)
    arr = np.array(img)
    length = len(arr)
    width = len(arr[1])
    step = 255 // (gradation - 1)

    for row in range(0, length, element_side):
        for col in range(0, width, element_side):
            midBright = mid_bright(arr, row, col, element_side)
            set_grey(arr, midBright, row, col, element_side, step)

    res = Image.fromarray(arr)
    res.save('res.jpg')

    return res


transform_img('img2.jpg', 2, 5)

