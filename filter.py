from PIL import Image
import numpy as np


def pixel_colors_sum(elements):
    n1 = elements[0]
    n2 = elements[1]
    n3 = elements[2]
    return int(n1) + int(n2) + int(n3)


def calculate_average_value(arr, y, x):
    result = 0
    count = blockSize * blockSize
    for row in range(y, y + blockSize):
        for col in range(x, x + blockSize):
            result += pixel_colors_sum(arr[row][col])
    return result // count


def set_grey_color(arr, averageValue, blockSize, i, j, step):
    for row in range(i, i + blockSize):
        for col in range(j, j + blockSize):
            greyValue = averageValue // 50 * step // 3
            arr[row][col][0] = greyValue
            arr[row][col][1] = greyValue
            arr[row][col][2] = greyValue


def transform_image(file_name, gradation, blockSize):
    image = Image.open(file_name)
    arr = np.array(image)
    height = len(arr)
    width = len(arr[1])
    step = 255 // gradation

    for i in range(0, height, blockSize):
        for j in range(0, width, blockSize):
            averageValue = calculate_average_value(arr, i, j)
            set_grey_color(arr, averageValue, blockSize, i, j, step)

    return Image.fromarray(arr)


gradation = 5
blockSize = 10

res = transform_image("img2.jpg", gradation, blockSize)
res.save('res.jpg')
