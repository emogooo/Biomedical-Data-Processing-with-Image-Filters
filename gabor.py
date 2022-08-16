import numpy as np
import cv2
g_kernel = cv2.getGaborKernel((45, 45), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)
img = cv2.imread('a.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtered_img = cv2.filter2D(img, cv2.CV_8UC3, g_kernel)
h, w = g_kernel.shape[:2]
g_kernel = cv2.resize(filtered_img, (3*w, 3*h), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('gabor.jpg', g_kernel)
