# Загрузить библиотеку
import cv2
import numpy as np 
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
# image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Загрузить изображение
image_bgr = cv2.imread("images/plane.jpg")

# Уведичить контраст изображения
# image_enhanced = cv2.equalizeHist(image)

# Конвентировать в YUV
image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)

# Выполнить выравнивание гистограммы
image_yuv[:, :, 0] = cv2.equalizeHist(image_yuv[:, :, 0])

# Конвентировать в RGB
image_rgb = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

# Вывести изображение
plt.imshow(image_rgb)
plt.axis("off")
plt.show()

# Сохранить изображение
# cv2.imwrite("images/plane_enhanced.jpg", image_enhanced)

# Сохранить изображение
cv2.imwrite("images/plane_enhanced_yuv.jpg", image_rgb)