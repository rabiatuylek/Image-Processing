# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:16:20 2020

@author: Rabia Tüylek
"""
import cv2
import os 
os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = "0"

#%% Color Filtering Hue Saturation Value (hsv)

book = cv2.imread("./images/book.jpg")
# boyut çok büyük, küçültmemiz lazım
book = cv2.resize(book,(1000,720))

hsv = cv2.cvtColor(book, cv2.COLOR_BGR2HSV)

lower_green = (26,77,68)
upper_green = (54,189,255)

mask = cv2.inRange(hsv,lower_green, upper_green)
#mask işlemi sonrası : arkayı siyah yapar, tek renge odaklanır.
final = cv2.bitwise_and(book, book, mask = mask)

cv2.imshow("original ımage", book)
cv2.imshow("masked image",mask)
cv2.imshow("final image",final)

cv2.waitKey(0)
cv2.destroyAllWindows()



#%% Video color filtering

live_cam = cv2.VideoCapture(0)
lower_green = (21,35,105)
upper_green = (58, 255, 243)

while(live_cam.isOpened()):
    
    ret,frame = live_cam.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,lower_green, upper_green)
    final_frame = cv2.bitwise_and(frame,frame, mask = mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("final frame", final_frame)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    
live_cam.release()
cv2.destroyAllWindows()














