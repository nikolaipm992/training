# Загрузить библиотеку
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Сохранить изображение
cv2.imwrite("images/plane_new.jpg", image)