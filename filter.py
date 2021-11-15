from PIL import Image
import numpy as np


def main():
    img = Image.open("img2.jpg")

    img_data = np.array(img)
    img_size = img_data.shape
    mosaic_size = 10
    grayscale_step = 50

    for x in range(0, img_size[0], mosaic_size):
        for y in range(0, img_size[1], mosaic_size):
            avg_brightness = get_avg_brightness(img_data, mosaic_size, x, y)
            apply_grayscale(img_data, mosaic_size, grayscale_step, x, y, avg_brightness)

    result = Image.fromarray(img_data)
    result.save("res.jpg")


def apply_grayscale(img_data, mosaic_size, grayscale_step, x, y, avg_brightness):
    for x1 in range(x, x + mosaic_size):
        for y1 in range(y, y + mosaic_size):
            img_data[x1][y1][0] = img_data[x1][y1][1] = img_data[x1][y1][2] = (
                int(avg_brightness // grayscale_step) * grayscale_step
            )


def get_avg_brightness(img_data, mosaic_size, x, y):
    avg_brightness = 0
    for x1 in range(x, x + mosaic_size):
        for y1 in range(y, y + mosaic_size):
            avg_brightness += int(sum(img_data[x1][y1])) // 3
    return int(avg_brightness // mosaic_size ** 2)


if __name__ == "__main__":
    main()
