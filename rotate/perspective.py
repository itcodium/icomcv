from scipy import misc
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')
rows,cols,ch = img.shape

print "img.shape",img.shape


M = cv2.getRotationMatrix2D((cols/2,rows/2),-0.25,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imwrite("rotate.jpg", dst)
	
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
