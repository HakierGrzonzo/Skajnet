from PIL import ImageFont, ImageDraw, Image
import numpy as np
import string
import random
import cv2
import csv

def genRand(x):
	return int(x*0.5-x*(np.random.rand(1)[0]))
def genFloatRand(x):
	return x*0.5-x*(np.random.rand(1)[0])
def distortImage(img):
	rows,cols = img.shape[:2]
	M = cv2.getRotationMatrix2D((cols/2,rows/2),genFloatRand(40),1)
	img = cv2.warpAffine(img,M,(cols,rows))
	
	pts1 = np.float32([[10+genFloatRand(25),10+genFloatRand(25)],[90+genFloatRand(25),10+genFloatRand(25)]
	,[90+genFloatRand(25),90+genFloatRand(25)],[10+genFloatRand(25),90+genFloatRand(25)]])
	pts2 = np.float32([[0,0],[150,0],[150,150],[0,150]])
	
	M2 = cv2.getPerspectiveTransform(pts1,pts2)
	img = cv2.warpPerspective(img,M2,(170,170))
	return img
def genFontName():
	return 'Font'+str(int(np.random.rand(1)[0]*26)+1)+'.ttf'
def genRandomChar():
	return random.choices(string.ascii_uppercase+string.digits)
File = open("dataset.txt",'w')
def genImagePair(count):
	name = genFontName()
	print(name)
	char = genRandomChar()[0]
	File.write(char+',')
	height,width = 170,170
	img = np.zeros((height,width,3),np.uint8)
	cv2_im_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	pil_im = Image.fromarray(cv2_im_rgb)
	draw = ImageDraw.Draw(pil_im)
	font = ImageFont.truetype('Fonts/'+name,49)
	draw.text((35+genRand(10),35+genRand(10)),char,font = font)
	img = cv2.cvtColor(np.array(pil_im),cv2.COLOR_RGB2BGR)
	#font = cv2.FONT_HERSHEY_SIMPLEX
	#cv2.putText(img,'9',(20+(genRand(18)-9),80+(genRand(18)-9)),font,2,(255,255,255),2,cv2.LINE_AA)
	img = distortImage(img)
	cv2.imwrite('image'+str(count)+'.png',img)
def genSet(count):
	for x in range(count):
		genImagePair(x)
