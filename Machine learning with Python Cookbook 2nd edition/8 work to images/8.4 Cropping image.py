# Загрузить библиотеку
import cv2
import numpy as np 
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Выбраь первую половину столбцов и все строки
image_cropped = image[:,:128]

# Вывести изображение
plt.imshow(image_cropped, cmap="gray")
plt.axis("off")
plt.show()

# Сохранить изображение
cv2.imwrite("images/plane_cropped.jpg", image_cropped)