from PIL import Image
import numpy as np
from numpy import ndarray

def grey_filter(img: Image, Size: int, Grey: int) -> Image:
    Pixels = np.array(img)
    Height = len(Pixels)
    Width = len(Pixels[1])
    for i in range(0, Width, Size):
        for j in range(0, Height, Size):
            averageCol = average_color(Pixels, i, j, Size)
            put_grey_on_pixels(Pixels, i, j, averageCol, Size, Grey)
    result_image = Image.fromarray(Pixels)
    return result_image


def average_color(img_pixels: ndarray, width: int, height: int, Size: int) -> int:
    RightWidth = out_of_bounds_value_for_width(img_pixels, width, Size)
    RightHeight = out_of_bounds_value_for_height(img_pixels, height, Size)
    averageCol = int(np.average(np.average(img_pixels[height: RightHeight, width: RightWidth])))
    return averageCol

def put_grey_on_pixels(img_pixels: ndarray, width: int, height: int, 
                       averageCol: int, Size: int, Grey: int) -> None:
    RightWidth = out_of_bounds_value_for_width(img_pixels, width, Size)
    RightHeight = out_of_bounds_value_for_height(img_pixels, height, Size)
    img_pixels[height: RightHeight, width: RightWidth] = \
    [averageCol // Grey * Grey] * 3

def out_of_bounds_value_for_height(img_pixels: ndarray, start_value: int, Size: int) -> int:
    img_height = len(img_pixels)
    if start_value + Size > img_height:
        return start_value + Size - (start_value + Size) % img_height
    return start_value + Size

def out_of_bounds_value_for_width(img_pixels: ndarray, start_value: int, Size: int) -> int:
    img_width = len(img_pixels[1])
    if start_value + Size > img_width:
        return start_value + Size - (start_value + Size) % img_width
    return start_value + Size

start_file = input("Вставьте название изображения:")
start_img = Image.open(start_file)
Size = int(input("Вставьте размер мозаики:"))
grey = int(input("Вставьте градацию серого:"))
res = grey_filter(start_img, Size, grey)
res.save("res.jpg")
print("Результат сохранён в res.jpg")

