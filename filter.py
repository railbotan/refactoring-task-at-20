from PIL import Image
import numpy as np


def do_filter(count_gradations, mosaic_size):
    img = Image.open("img2.jpg")
    arr = np.array(img)
    width = len(arr)
    height = len(arr[1])
    gradations = 255 // count_gradations
    pixel_x = 0

    def find_average_brightness(array, px_width, px_height, mosaic):
        sum_brightness = 0
        for cell_pixel_x in range(px_width, px_width + mosaic):
            for cell_pixel_y in range(px_height, px_height + mosaic):
                px_coord = array[cell_pixel_x][cell_pixel_y]
                r = px_coord[0]
                g = px_coord[1]
                b = px_coord[2]
                median = r // 3 + g // 3 + b // 3
                sum_brightness += median
        average_bright = int(sum_brightness // mosaic_size ** 2)
        return average_bright

    def paint_cell(array, px_width, px_height, mosaic):
        for cell_pixel_x in range(px_width, px_width + mosaic):
            for cell_pixel_y in range(px_height, px_height + mosaic):
                px_coord = array[cell_pixel_x][cell_pixel_y]
                px_coord[0] = int(average_brightness // gradations) * gradations
                px_coord[1] = int(average_brightness // gradations) * gradations
                px_coord[2] = int(average_brightness // gradations) * gradations

    while pixel_x < width - mosaic_size + 1:
        pixel_y = 0
        while pixel_y < height - mosaic_size + 1:
            average_brightness = find_average_brightness(arr, pixel_x, pixel_y, mosaic_size)
            paint_cell(arr, pixel_x, pixel_y, mosaic_size)
            pixel_y = pixel_y + mosaic_size
        pixel_x = pixel_x + mosaic_size
    res = Image.fromarray(arr)
    res.save('res.jpg')


do_filter(10, 52)