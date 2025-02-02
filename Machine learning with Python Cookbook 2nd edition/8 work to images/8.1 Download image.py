# Загрузить библиотеку
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
# image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Загрузить цветное изображение
image_bgr = cv2.imread("images/plane.jpg", cv2.IMREAD_COLOR)

# Преобразовать в RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Вывести пикселы
print(image_bgr[0,0])

# Вывести тип данных
# print(type(image))

# Вывести данные изображения
# print(image)

# Вывести размер
# print(image.shape)

# Вывести первый пиксел
# print(image[0,0])

# Вывести изображение
# plt.imshow(image, cmap="gray")
plt.imshow(image_rgb)

plt.axis("off")
plt.show()