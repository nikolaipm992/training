# Загрузить библиотеку
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Изменить размер на 50х50 пикселов
image_50x50 = cv2.resize(image, (50, 50))

# Вывести изображение
plt.imshow(image_50x50, cmap="gray")
plt.axis("off")
plt.show()

# Сохранить изображение
cv2.imwrite("images/plane_50x50.jpg", image_50x50)