from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                r = arr[n][n1][0]
                g = arr[n][n1][1]
                b = arr[n][n1][2]
                s += (int(r) + int(g) + int(b)) // 3
        mid_bright = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(mid_bright // 50) * 50
                arr[n][n1][1] = int(mid_bright // 50) * 50
                arr[n][n1][2] = int(mid_bright // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')

