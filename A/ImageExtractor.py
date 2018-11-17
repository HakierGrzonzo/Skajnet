import numpy as np
from matplotlib import pyplot as plt
import math
import cv2
def getContrast(filename):
	img = cv2.imread(filename,0)
	array = np.array(img)
	array = np.divide(array,255*1.49)
	array = np.round(array)
	#print(array[0][34])
	plt.imshow(array)
	plt.show()
	return array
getContrast('0_56_right_18.jpg')