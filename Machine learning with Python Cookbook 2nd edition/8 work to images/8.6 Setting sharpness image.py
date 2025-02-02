# Загрузить библиотеку
import cv2
import numpy as np 
from matplotlib import pyplot as plt

# Загрузить изображение в оттенках серого
image = cv2.imread("images/plane.jpg", cv2.IMREAD_GRAYSCALE)

# Создать ядро
kernel =np.array([[0, -1, 0],
                  [-1, 5, -1],
                  [0, -1, 0]])

# Изменить резкость изображений
image_sharp = cv2.filter2D(image, -1, kernel)

# Вывести изображение
plt.imshow(image_sharp, cmap="gray")
plt.axis("off")
plt.show()

# Сохранить изображение
cv2.imwrite("images/plane_sharp.jpg", image_sharp)