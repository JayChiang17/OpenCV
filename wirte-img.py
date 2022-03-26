# -*- coding:UTF-8 -*-
import cv2
import numpy as np


img = np.zeros((600,600,3),np.uint8)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,0,255),2) #畫線

cv2.rectangle(img,(100,100) ,(400,300), (0,255,0), cv2.FILLED) #畫方型(並填滿)

cv2.circle(img, (300,400), 50, (255,0,0), cv2.FILLED)#畫圓

cv2.putText(img, "HELLO", (100,500), cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2) #寫字

cv2.imshow('img',img)
cv2.waitKey(0)