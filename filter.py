from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
size = 2
gradation = 50
a = len(arr)
a1 = len(arr[1])


def findMidValue(i, j, size):
    s=0
    global arr
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            r = arr[n][n1][0]
            g = arr[n][n1][1]
            b = arr[n][n1][2]
            M = int(r) + int(g) + int(b)
            s += M / 3
    s = int(s // size**2)
    return s


def changeColour(i, j, size, gradation):
    global arr
    s = findMidValue(i, j, size)
    for n in range(i, i + size):
        for n1 in range(j, j + size):
            arr[n][n1][0] = np.uint8((s // gradation) * gradation)
            arr[n][n1][1] = np.uint8((s // gradation) * gradation)
            arr[n][n1][2] = np.uint8((s // gradation) * gradation)


i = 0
while i <= a - 1:
    j = 0
    while j <= a1 - 1:
        changeColour(i, j, size, gradation)
        j = j + size
    i = i + size
res = Image.fromarray(arr)
res.save('res.jpg')
