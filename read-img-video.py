# -*- coding:UTF-8 -*-
import cv2

# img = cv2.imread('monster.jpg')
# img = cv2.resize(img, (0,0), fx=2, fy=2) #fx, fy times 2
# cv2.imshow('img',img) #show img
# cv2.waitKey(5000) #show 1000 ms time when someone click the keybourd

cap = cv2.VideoCapture(0) #取得檔案名，或是使用 0 取得電腦鏡頭
while True:
    ret, frame = cap.read() #取得每一幀 ret=bool frame＝如果有成功讀取下一幀
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    if ret:
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(1) == ord('q'): #按p之後跳出
        break
