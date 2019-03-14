#cv2.split() splits rgb channels
#cv2.merge() joins the channels
import cv2
import numpy as np
import math

img=cv2.imread('kitten.jpg')

imgColored=(4*img/255).round()*(255/4)
err=imgColored-img
cv2.imshow('Colored!!',imgColored)
cv2.waitKey(0)
