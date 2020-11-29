# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:32:33 2020

@author: Rabia Tüylek
"""
#importing libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%% Reading an image

image = cv2.imread("Logo.png")
cv2.imshow("open cv", image)
#writing an image
cv2.imwrite("./logo_gri.png", image)

cv2.waitKey(0)
cv2.destroyAllwindows()
#%% Some basic features

picture = cv2.imread("pug.jpg")
#print(picture.show)

my_pixel = picture[220,13,:]
b,g,r = cv2.split(picture)

print("Blue",my_pixel[0])
print("Green",my_pixel[1])
print("Red",my_pixel[2])

cv2.imshow("dog",picture)

cv2.waitKey(0)
cv2.destroyAllwindows()

#%% Conveerting Image to Gray , HSV
scenery = cv2.imread("scenery.jpg")

scenery_gray=cv2.cvtColor(scenery, cv2.COLOR_BGR2GRAY)
scenery_hsv=cv2.cvtColor(scenery, cv2.COLOR_BGR2HSV)
scenery_hls=cv2.cvtColor(scenery, cv2.COLOR_BGR2HLS)
scenery_bgra=cv2.cvtColor(scenery, cv2.COLOR_BGR2BGRA)
scenery_cıe=cv2.cvtColor(scenery, cv2.COLOR_BGR2XYZ)

cv2.imshow("original",scenery)
cv2.imshow("gray",scenery_gray)
cv2.imshow("HSV",scenery_hsv)
cv2.imshow("HLS",scenery_hls)
cv2.imshow("BGRA",scenery_bgra)
cv2.imshow("CIE",scenery_cıe)

cv2.waitKey(0)
cv2.destroyAllwindows()

#%% Splitting and showing one channel of image

B,G,R = cv2.split(picture)
picture= cv2.merge((B,G,R))

cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.imshow("original",picture)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
deneme_img = cv2.imread("Logo.png")
cv2.imshow("original",deneme_img)
b,g,r = cv2.split(deneme_img)

cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)

cv2.waitKey(0)
cv2.destroyAllWindows()

#%% Seeing the openCV logo as 2 channels
copy1 = deneme_img.copy()
copy2 = deneme_img.copy()
copy3 = deneme_img.copy()
 
copy1[:,:,2] = 0 # no red
copy2[:,:,1] = 0 # no green
copy3[:,:,0] = 0 # no blue

cv2.imshow("original",deneme_img)
cv2.imshow("no red", copy1)
cv2.imshow("no green", copy2)
cv2.imshow("no blue", copy3)

cv2.waitKey(0)
cv2.destroyAllWindows()










