# Загрузить библиотеку
import cv2
import numpy as np 
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Усреднить изображение
# image_blurry = cv2.blur(image, (5,5))

# Усреднить изображение
# image_very_blurry = cv2.blur(image, (100,100))

# Вывести изображение
# plt.imshow(image_blurry, cmap="gray")
# plt.axis("off")
# plt.show()

# Вывести изображение
# plt.imshow(image_very_blurry, cmap="gray")
# plt.xticks([])
# plt.yticks([])
# plt.show()


# Создать ядро
kernel =np.ones((5,5)) / 25.0

# Вывести ядро на экран
print(kernel)

# Применить ядро
image_kernel = cv2.filter2D(image, -1, kernel)

# Вывести изображение
plt.imshow(image_kernel, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()

# Сохранить изображение
# cv2.imwrite("images/plane_blur.jpg", image_blurry)

# Сохранить изображение
# cv2.imwrite("images/plane_very_blur.jpg", image_very_blurry)

# Сохранить изображение
cv2.imwrite("images/plane_kernel.jpg", image_kernel)