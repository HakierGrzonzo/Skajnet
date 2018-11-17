import numpy as np
from matplotlib import pyplot as plt
import math
import cv2
def round(x):
	x/=255
	if x>0.75:
		return 1
	return 0
def scale(x):
	return [round(y) for y in x]
img = cv2.imread('0_51_right_13.jpg',0)
array = np.array(img)
array = np.divide(array,255*1.49)
array = np.round(array)
print(array[0][34])
plt.imshow(array)
plt.show()