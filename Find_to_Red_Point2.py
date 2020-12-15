# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 15:06:47 2020

@author: Rabia Tüylek
"""
import numpy as np
import cv2
import os
os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = "0"

camera = cv2.VideoCapture(0)
lower_red = (170,50,50)
upper_red =(180,255,255)

kernel = np.ones((5,5),np.uint8)

while (camera.isOpened()):
    ret , frame = camera.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    wanted_video = cv2.bitwise_and(frame, frame, mask = mask)
    
    mask = cv2.erode(mask,kernel,iterations=1)
    mask = cv2.dilate(mask,kernel,iterations=1)
    
    contors = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) [-2]
    cv2.drawContours(frame,contors, -1,(255,0,0),3)
    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("wanted", wanted_video)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
            
camera.release()
cv2.destroyAllWindows()
    
    



