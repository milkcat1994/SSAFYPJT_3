
from anonymize_face_pixelate import anonymize_face_pixelate
from anonymize_face_simple import anonymize_face_simple
import numpy as np
import cv2
import argparse
import sys
import os

tempVar = [[2056,2419,150,513], [805,1201,141,537]]
def isSame(y,ey,x,ex):
	for tv in tempVar:
		if np.array_equal(tv, np.array([y,ey,x,ex])):
			return True
	return False

# 입력 파일 저징하기
image_file = ".\\imgs\\earring.jpg"

# 캐스테이드 파일의 경로 지정하기
cascade_file = ".\\cascade\\haarcascade_frontalface_alt.xml"

# 이미지 읽어 들이기
image = cv2.imread(image_file)
# print(image)

# 그레이스케일로 변환하기
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 인식 특징 파일 읽어 들이기
cascade = cv2.CascadeClassifier(cascade_file)
# 얼굴 인식 실행하기
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

if len(face_list) > 0:
	# 인식한 부분 표시하기
	print(face_list)
	color = (0, 0, 255)
	for face in face_list:
		x, y, w, h = face
		face2 = image[y:y+h, x:x+w]
		if not isSame(y,y+h,x,x+w) :
			face2 = anonymize_face_simple(face2, factor=3.0)
			image[y:y+h, x:x+w] = face2

        # cv2.rectangle(image, (x, y), (x+w, y+h), color, thickness=8)

	# 파일로 출력하기
	cv2.imwrite(".\\result\\tongchun-facedetect.png", image)

else:
	print("no face") 