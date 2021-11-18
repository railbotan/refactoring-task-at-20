from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
size = 10
gradation = 50
a = len(arr)
a1 = len(arr[1])


def findMidValue(i, j, size):
    global arr
    matrix = arr[i:i + size, j:j + size, ::]
    b = list(matrix.reshape(1, matrix.shape[0] * matrix.shape[1] * 3))[0]
    b = list(map(lambda x: int(x)/3, b))
    s = int(sum(b)// size**2)
    return s


def changeColour(i, j, size, gradation):
    global arr
    s = findMidValue(i, j, size)
    arr[i:i + size, j:j + size, ::] = s


i = 0
while i <= a - 1:
    j = 0
    while j <= a1 - 1:
        changeColour(i, j, size, gradation)
        j = j + size
    i = i + size
res = Image.fromarray(arr)
res.save('res.jpg')
