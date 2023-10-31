from PIL import Image
import numpy as np
from time import sleep
import os

to_copy = ""
cont = 0
SIZE = (100,100)
while cont < 6571:
    os.system('cls')
    image = Image.open(f"./frames/frame{cont}.jpg")
    image = image.convert('1')
    image_array = np.asarray(image)
    image_array = np.where(image_array == 0, '■', '')
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            print(image_array[i][j], end=" ", flush=True)
        print()
    sleep(1/30)
    cont += 1