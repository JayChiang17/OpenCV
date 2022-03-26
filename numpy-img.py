from hashlib import new
import cv2
import numpy as np
import random

img = cv2.imread('monster.jpg')

# img = np.empty((300,300,3), np.uint8)

# for row in range(300):
#     for col in range(300):
#         img[row][col] = [random.randint(0,255), 0,255]
newImg = img[:150, 200:400]

cv2.imshow('newImg',newImg)
cv2.waitKey(0)
