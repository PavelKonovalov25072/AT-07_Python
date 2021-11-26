from PIL import Image
import numpy as np
from numpy import ndarray


def grey_filter(img: Image, size: int, Grey: int) -> Image:
    Pixels = np.array(img)
    Height = len(Pixels)
    Width = len(Pixels[1])
    for i in range(0, Width, size):
        for j in range(0, Height, size):
            averageCol = average_color(Pixels, i, j, size)
            put_grey_on_pixels(Pixels, i, j, averageCol, size, Grey)
    result_image = Image.fromarray(Pixels)
    return result_image


def average_color(img_pixels: ndarray, width: int, height: int, size: int) -> int:
    RightWidth = out_of_bounds_value_for_width(img_pixels, width, size)
    RightHeight = out_of_bounds_value_for_height(img_pixels, height, size)
    averageCol = int(np.average(np.average(img_pixels[height: RightHeight, width: RightWidth])))
    return averageCol


def put_grey_on_pixels(img_pixels: ndarray, width: int, height: int,
                       averageCol: int, size: int, Grey: int) -> None:
    RightWidth = out_of_bounds_value_for_width(img_pixels, width, size)
    RightHeight = out_of_bounds_value_for_height(img_pixels, height, size)
    img_pixels[height: RightHeight, width: RightWidth] = \
        [averageCol // Grey * Grey] * 3


def out_of_bounds_value_for_height(img_pixels: ndarray, start_value: int, size: int) -> int:
    img_height = len(img_pixels)
    if start_value + size > img_height:
        return start_value + size - (start_value + size) % img_height
    return start_value + size


def out_of_bounds_value_for_width(img_pixels: ndarray, start_value: int, size: int) -> int:
    img_width = len(img_pixels[1])
    if start_value + size > img_width:
        return start_value + size - (start_value + size) % img_width
    return start_value + size


start_img = Image.open("img2.jpg")
Size = int(10)
grey = int(50)
res = grey_filter(start_img, Size, grey)
res.save("res2.jpg")
print("Результат сохранён в res.jpg")
