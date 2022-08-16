from skimage.io import imread
from skimage.transform import resize
from skimage.feature import hog
import matplotlib.pyplot as plt

img = imread('a.jpg')
plt.axis("off")
plt.imshow(img)
resized_img = resize(img, (64*4, 32*4))
plt.axis("off")
plt.imshow(resized_img)
fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
plt.axis("off")
plt.imshow(hog_image, cmap="gray")