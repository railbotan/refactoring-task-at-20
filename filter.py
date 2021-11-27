from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 11:
    j = 0
    while j < a1 - 11:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                n1 = arr[n][n1][0]
                n2 = arr[n][n1][1]
                n3 = arr[n][n1][2]
                M = n1 + n2 + n3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')

def main():
    imageLocation = input("Путь к фото:")
    resultName = input("Название результата:")
    mosaicSize = int(input("Размер мозайки в пикселях:"))
    gradationsCount = int(input("Количество градаций серого:"))
    imageData = np.array(Image.open(imageLocation))
    imageSize = imageData.shape

    for x in range(0, imageSize[0], mosaicSize):
        for y in range(0, imageSize[1], mosaicSize):
            paintCell(imageData, x, y, mosaicSize, gradationsCount)

    res = Image.fromarray(imageData)
    outputLocation = imageLocation[0:imageLocation.rindex('\\') + 1]
    res.save(f"{outputLocation}{resultName}")

def paintCell(array, pxWidth, pxHeight, mosaicSize, gradationsCount):
    averageBrightness = findAverageBrightness(array, pxWidth, pxHeight, mosaicSize)
    gradations = 255 // gradationsCount
    pxBrightness = averageBrightness // gradations * gradations
    array[pxWidth:pxWidth + mosaicSize, pxHeight:pxHeight + mosaicSize, ][:] = pxBrightness
    
def findAverageBrightness(array, pxWidth, pxHeight, mosaicSize):
    return np.average(array[pxWidth:pxWidth + mosaicSize, pxHeight: pxHeight + mosaicSize])
