from PIL import Image
import numpy as np


def get_mid_bright(block, element_side, step):
    midBright = block[:element_side, :element_side].sum() // (element_side * element_side)
    return int(midBright // step) * step / 3


def transform_img(image_file, element_side, gradation):
    img = Image.open(image_file)
    arr = np.array(img)
    length = len(arr)
    width = len(arr[1])
    step = 255 // (gradation - 1)

    for row in range(0, length, element_side):
        for col in range(0, width, element_side):
            arr[row: row + element_side, col: col + element_side] = get_mid_bright(
                arr[row: row + element_side, col: col + element_side], element_side, step
            )
    res = Image.fromarray(arr)
    res.save('res.jpg')

    return res


transform_img('img2.jpg', 2, 5)

