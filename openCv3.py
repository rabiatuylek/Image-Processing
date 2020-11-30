# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:10:53 2020

@author: Rabia Tüylek
"""

import cv2
import os

os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = "0"
#%% Resolution Changing
resolution = {"width": 200, "height": 100}
pug = cv2.imread("./images/pug.jpg")
img = cv2.imread("./images/pug.jpg")

new_width = resolution["width"]/pug.shape[1]
new_height = resolution["height"]/pug.shape[0]

scale = min(new_width,new_height)
# for width = 1
#for height = 0
my_width = int(img.shape[1]*scale)
my_height = int(img.shape[0]*scale)

name = "new_window"

cv2.namedWindow(name,cv2.WINDOW_NORMAL)
cv2.resizeWindow(name, my_width, my_height)

cv2.imshow(name,pug)
cv2.imshow("pug",pug)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% image pyramids (gaussian pyramid)
nature = cv2.imread("./images/nature.jpg")
#resmi küçültmek
lower_nature = cv2.pyrDown(nature)
# resmi büyültmek
higher_nature = cv2.pyrUp(nature)

cv2.imshow("lower", lower_nature)
cv2.imshow("up",higher_nature)
cv2.imshow("original",nature)

cv2.waitKey(0)
cv2.destroyAllWindows() 

#%% Drawing circle

acm = cv2.imread("./images/acm.png")
#şekil çizeceğimiz resmi copy ile çoğaltmalıyız.
rectangle = acm.copy()
circle = acm.copy()
text = acm.copy()

cv2.imshow("acm",acm)

starting_point = (550,200)
ending_point = (1360,700)
border_colour = (255,0,255)
thickness = 5

rectangle = cv2.rectangle(rectangle, starting_point,ending_point, border_colour, thickness)

center = (960,450)
radius = 400
circle = cv2.circle(circle,center,radius,border_colour, thickness)


bottom_left_point = (600,570)
my_text = "welcomee to image processing world ! "
my_text = cv2.putText(text,my_text, bottom_left_point,cv2.FONT_HERSHEY_COMPLEX, 1.0,color = border_colour )



cv2.imshow("Rectangle", rectangle)
cv2.imshow("circle",circle)
cv2.imshow("Text",text)
cv2.waitKey(0)
cv2.destroyAllWindows()




































