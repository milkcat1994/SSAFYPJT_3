from __future__ import division
import torch
import os
import cv2
import numpy as np
from .common.utils import BBox
from .models.pfld_compressed import PFLDInference
from PIL import Image
from .MTCNN import detect_faces
import glob
import face_recognition as fr
import math

import random 

# for global variable
from django.conf import settings

# MODEL_URL = settings.MODEL_URL
SWAP_URL = settings.SWAP_URL
import base64

from django.conf import settings

IMAGES_URL = settings.IMAGES_URL

def extract_index_nparray(nparray):
    index = None
    for num in nparray[0]:
        index = num
        break
    return index

# 전달받은 url을 파일의 절대 경로로 변경
'''
url : 절대 경로로 바꾸어 줄 url
'''
def change_url_to_absolute(url):
    # localhost
    # abs_path = ""
    # AWS
    abs_path = IMAGES_URL
    return abs_path+url

# 이미지 blur 처리 함수
'''
image : blur 처리할 crop된 image
factor : blur 처리할 강도 (default=3.0)
'''
def anonymize_face_simple(image, factor=3.0):
	# automatically determine the size of the blurring kernel based
	# on the spatial dimensions of the input image
	(h, w) = image.shape[:2]
	kW = int(w / factor)
	kH = int(h / factor)
	# ensure the width of the kernel is odd
	if kW % 2 == 0:
		kW -= 1
	# ensure the height of the kernel is odd
	if kH % 2 == 0:
		kH -= 1
	# apply a Gaussian blur to the input image using our computed
	# kernel size
	return cv2.GaussianBlur(image, (kW, kH), 0)
    
# 이미지 pixel 처리 함수
'''
image : pixel 처리할 crop된 image
factor : pixel 처리할 강도 (default=3.0)
'''
def anonymize_face_pixelate(image, blocks=3):
	# divide the input image into NxN blocks
	(h, w) = image.shape[:2]
	xSteps = np.linspace(0, w, blocks + 1, dtype="int")
	ySteps = np.linspace(0, h, blocks + 1, dtype="int")
	# loop over the blocks in both the x and y direction
	for i in range(1, len(ySteps)):
		for j in range(1, len(xSteps)):
			# compute the starting and ending (x, y)-coordinates
			# for the current block
			startX = xSteps[j - 1]
			startY = ySteps[i - 1]
			endX = xSteps[j]
			endY = ySteps[i]
			# extract the ROI using NumPy array slicing, compute the
			# mean of the ROI, and then draw a rectangle with the
			# mean RGB values over the ROI in the original image
			roi = image[startY:endY, startX:endX]
			(B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
			cv2.rectangle(image, (startX, startY), (endX, endY),
				(B, G, R), -1)
	# return the pixelated blurred image
	return image


# blur, pixel에 대한 수정 옵션 강도 반환 함수
'''
option_type : 'blur', 'pixel'과 같은 수정옵션
option_level : 해당 수정옵션에 적용할 강도 (1~5)
'''
def weights(option_type, option_level):
    return {
        'blur':[1., 1., 2., 3., 4., 5.],
        'pixel':[1., 3., 5., 7., 9., 11.]
    }.get(option_type)[option_level]


# 사진 세부 수정 호출 함수
'''
option_type : blur, pixel, swap, sticker
img : 원본 이미지
swap_area : 수정할 사각형 좌표
option_level : blur, pixel의 강도
sticker : 스티커 이미지
'''
def face_transform(option_type, img, swap_area, option_level, sticker):
    if option_type == 'blur':
        res_img = blur(img, swap_area, option_level)
    elif option_type == 'pixel':
        res_img = pixel(img, swap_area, option_level)
    elif option_type == 'swap':
        res_img = face_swap(img, swap_area)
    elif option_type == 'sticker':
        res_img = sticker_swap(img, swap_area, sticker)
        
    else:
        print("No option_type(" + option_type + ")" )
        res_img = None
    # 파일로 출력하기
    # cv2.imwrite(".\\results\\result.png", img)

    _, im_arr = cv2.imencode('.jpg', res_img)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    img_crop_b64 = base64.b64encode(im_bytes)

    return img_crop_b64


#테스트용 matplotlib
# from matplotlib import pyplot as plt

# 얼굴 찾기 및 친구 얼굴 반환
'''
list : 얼굴만 crop된 사각형 좌표
faces_crop : 얼굴만 crop된 이미지들
friend_list :
{
  'fname': '이름',
  'square': 사각형좌표,
  'idx':list의 해당 image index
}
'''
def face_detection(img, friends):
    faces_area=[]
    faces_crop=[]
    friend_dic={}
    friend_list=[]

    friend_crop_img_list=[]
    for friend in friends:
        friend_crop_img_list.append(fr.face_encodings(cv2.imread(change_url_to_absolute(friend['img']))))

    height,width,_=img.shape
    # perform face detection using MTCNN
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)

    faces = detect_faces(image)

    if len(faces)==0:
        print('NO face is detected!')
        return [], [], []
        
    for k, face in enumerate(faces):
        x1=face[0]
        y1=face[1]
        x2=face[2]
        y2=face[3]
        w = x2 - x1 + 1
        h = y2 - y1 + 1
        size = int(min([w, h])*1.2)
        cx = x1 + w//2
        cy = y1 + h//2
        x1 = cx - size//2
        x2 = x1 + size
        y1 = cy - size//2
        y2 = y1 + size

        x1 = int(max(0, x1))
        y1 = int(max(0, y1))
        x2 = int(min(width, x2))
        y2 = int(min(height, y2))

        img_crop=img[y1:y2, x1:x2]
        # print(x1,x2,y1,y2)


        ####################################################
        _, im_arr = cv2.imencode('.jpg', img_crop)  # im_arr: image in Numpy one-dim array format.
        im_bytes = im_arr.tobytes()
        img_crop_b64 = base64.b64encode(im_bytes)
        faces_crop.append(img_crop_b64)
        ####################################################

        

        # faces_crop.append(img_crop)
        faces_area.append((x1, y1, x2, y2))

        # 등록되지 않은 얼굴을 128-dimensional face 인코딩
        enc_unknown_face = fr.face_encodings(img_crop, known_face_locations=[(0, x2-x1, y2-y1, 0)])

        for idx, friend in enumerate(friends):
            # print(friend)

            # 등록된 얼굴을 128-dimensional face 인코딩
            # enc_known_face = fr.face_encodings(friend_list[0])
            enc_known_face = friend_crop_img_list[idx]
            # 등록된 얼굴과 새로운 얼굴의 distance를 얻기 (유사도)
            # 1에 가까울수록 다른 사람 얼굴 이며, 보통 0.5이상이면 다른사람으로 인식한다.
            distance = fr.face_distance(enc_known_face, enc_unknown_face[0])
            # print(distance)
            # 제약을 0.35로 하여 친구 얼굴이 확실 할때만 체크한다.
            if distance < 0.35:
                if friend['fname'] in friend_dic:
                    friend_dic[friend['fname']] = {'distance': min(friend_dic[friend['fname']]['distance'], distance), 'square':list(map(int, [x1, y1, x2, y2])), 'idx':k}
                else:
                    friend_dic[friend['fname']] = {'distance': distance, 'square':list(map(int, [x1, y1, x2, y2])), 'idx':k}
                    # print(distance)
    


    # 친구라고 인식된 얼굴 보기
    # for friend in friend_dic:
    #     print(friend)
    #     plt.imshow(cv2.cvtColor(img[ceil(friend_dic[friend]['square'][1]):ceil(friend_dic[friend]['square'][3]),ceil(friend_dic[friend]['square'][0]):ceil(friend_dic[friend]['square'][2])], cv2.COLOR_RGB2BGR))
    #     plt.show()

    for friend in friend_dic:
        friend_list.append({'fname': friend, 'square': friend_dic[friend]['square'], 'idx':friend_dic[friend]['idx']})

    return faces_area, faces_crop, friend_list


# 넘겨받은 얼굴 영역 blur 처리 요청 함수
'''
img : 원본 image
swap_area : blur 처리 할 사각형 좌표
option_level : blur 처리 할 강도
'''
def blur(img, swap_area, option_level):
    factor = weights('blur', option_level)
    if factor is None:
        return img

    for face in swap_area:
        x1, y1, x2, y2 = face
        face2 = img[y1:y2, x1:x2]
        face2 = anonymize_face_simple(face2, factor)
        img[y1:y2, x1:x2] = face2
    return img


# 넘겨받은 얼굴 영역 pixel 처리 요청 함수
'''
img : 원본 image
swap_area : pixel 처리 할 사각형 좌표
option_level : pixel 처리 할 강도
'''
def pixel(img, swap_area, option_level):
    blocks = weights('pixel', option_level)
    if blocks is None:
        return img

    for face in swap_area:
        x1, y1, x2, y2 = face
        face2 = img[y1:y2, x1:x2]
        face2 = anonymize_face_pixelate(face2, blocks)
        img[y1:y2, x1:x2] = face2
    return img


# 가상 얼굴 교체
def face_swap(img, swap_area):
    img = cv2.resize(img, dsize=(0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    height, width, channels = img.shape
    img_new_face = np.zeros((height, width, channels), np.uint8)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    out_size = 112
    model = PFLDInference()

    path = os.path.dirname( os.path.abspath( __file__ ) ).replace("\\","/") + '/checkpoint/pfld_model_best.pth.tar'
    checkpoint = torch.load(path, map_location='cpu')
    # checkpoint = torch.load(MODEL_URL, map_location='cpu')

    #checkpoint = torch.load('checkpoint/pfld_model_best.pth.tar', map_location='cpu')
    model.load_state_dict(checkpoint['state_dict'])
    model = model.eval()

    for k in range(0, len(swap_area)):
        #face swap할 이미지 분석
        x1 = swap_area[k][0]*2
        y1 = swap_area[k][1]*2
        x2 = swap_area[k][2]*2
        y2 = swap_area[k][3]*2

        dx = max(0, -x1)
        dy = max(0, -y1)
        x1 = max(0, x1)
        y1 = max(0, y1)

        edx = max(0, x2 - width)
        edy = max(0, y2 - height)

        new_bbox = list(map(int, [x1, x2, y1, y2]))
        new_bbox = BBox(new_bbox)
        cropped = img[new_bbox.top:new_bbox.bottom, new_bbox.left:new_bbox.right]
        if (dx > 0 or dy > 0 or edx > 0 or edy > 0):
            cropped = cv2.copyMakeBorder(cropped, int(dy), int(edy), int(dx), int(edx), cv2.BORDER_CONSTANT, 0)
        cropped_face = cv2.resize(cropped, (out_size, out_size))

        if cropped_face.shape[0] <= 0 or cropped_face.shape[1] <= 0:
            continue
        test_face = cropped_face.copy()
        test_face = test_face / 255.0
        test_face = test_face.transpose((2, 0, 1))
        test_face = test_face.reshape((1,) + test_face.shape)
        input = torch.from_numpy(test_face).float()
        input = torch.autograd.Variable(input)


        landmark = model(input).cpu().data.numpy()
        landmark = landmark.reshape(-1, 2)
        landmark = new_bbox.reprojectLandmark(landmark)

        points = np.array(landmark, np.int32)
        convexhull = cv2.convexHull(points)
        landmarks_points = []

        for x, y in landmark:
            landmarks_points.append(( int(x), int(y) ))
            # cv2.circle(img, (int(x),int(y)), 1, (0,255,0),1)

        # cv2.imshow("s",img)
        # cv2.waitKey(0)
        
        random_number = random.randint(0, 311)
        
        img2 = cv2.imread(SWAP_URL+str(random_number)+".jpg")
        
        height2, width2, _ = img2.shape
        img2 =  cv2.resize(img2, dsize=(0, 0), fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
     
        
        img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        mask = np.zeros_like(img_gray2)

        new_face = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        new_face = Image.fromarray(new_face)
        face2 = list(map(int, detect_faces(new_face)[0]))

        new_bbox2 = list(map(int, [face2[0], face2[2], face2[1], face2[3]]))
        new_bbox2 = BBox(new_bbox2)
        cropped2 = img2[new_bbox2.top:new_bbox2.bottom, new_bbox2.left:new_bbox2.right]
        cropped2_face = cv2.resize(cropped2, (out_size, out_size))

        test_face2 = cropped2_face.copy()
        test_face2 = test_face2 / 255.0
        test_face2 = test_face2.transpose((2, 0, 1))
        test_face2 = test_face2.reshape((1,) + test_face2.shape)
        input2 = torch.from_numpy(test_face2).float()
        input2 = torch.autograd.Variable(input2)

        landmark2 = model(input2).cpu().data.numpy()
        landmark2 = landmark2.reshape(-1, 2)
        landmark2 = new_bbox2.reprojectLandmark(landmark2)
        points2 = np.array(landmark2, np.int32)

        convexhull2 = cv2.convexHull(points2)
        cv2.fillConvexPoly(mask, convexhull2, 255)

        rect2 = cv2.boundingRect(convexhull2)
        subdiv = cv2.Subdiv2D(rect2)

        landmarks_points2 = []
        for x, y in landmark2:
            landmarks_points2.append((int(x), int(y)))
        subdiv.insert(landmarks_points2)
        triangles = subdiv.getTriangleList()
        triangles = np.array(triangles, dtype=np.int32)
        indexes_triangles = []
        for t in triangles:
            pt1 = (t[0], t[1])
            pt2 = (t[2], t[3])
            pt3 = (t[4], t[5])

            index_pt1 = np.where((points2 == pt1).all(axis=1))
            index_pt1 = extract_index_nparray(index_pt1)

            index_pt2 = np.where((points2 == pt2).all(axis=1))
            index_pt2 = extract_index_nparray(index_pt2)

            index_pt3 = np.where((points2 == pt3).all(axis=1))
            index_pt3 = extract_index_nparray(index_pt3)

            if index_pt1 is not None and index_pt2 is not None and index_pt3 is not None:
                triangle = [index_pt1, index_pt2, index_pt3]
                indexes_triangles.append(triangle)

        img_face_mask = np.zeros_like(img_gray)
        img_head_mask = cv2.fillConvexPoly(img_face_mask, convexhull, 255)

        for triangle_index in indexes_triangles:
            # Triangulation of the first face2
            tr2_pt1 = landmarks_points2[triangle_index[0]]
            tr2_pt2 = landmarks_points2[triangle_index[1]]
            tr2_pt3 = landmarks_points2[triangle_index[2]]
            triangle2 = np.array([tr2_pt1, tr2_pt2, tr2_pt3], np.int32)

            rect2 = cv2.boundingRect(triangle2)
            (x, y, w, h) = rect2
            cropped_triangle = img2[y: y + h, x: x + w]

            cropped_tr2_mask = np.zeros((h, w), np.uint8)

            points2 = np.array([[tr2_pt1[0] - x, tr2_pt1[1] - y],
                                [tr2_pt2[0] - x, tr2_pt2[1] - y],
                                [tr2_pt3[0] - x, tr2_pt3[1] - y]], np.int32)

            cv2.fillConvexPoly(cropped_tr2_mask, points2, 255)

            # Triangulation of second face2
            tr1_pt1 = landmarks_points[triangle_index[0]]
            tr1_pt2 = landmarks_points[triangle_index[1]]
            tr1_pt3 = landmarks_points[triangle_index[2]]
            triangle = np.array([tr1_pt1, tr1_pt2, tr1_pt3], np.int32)

            # Lines space
            # cv2.line(img_new_face, tr1_pt1, tr1_pt2, (255, 255, 255))
            # cv2.line(img_new_face, tr1_pt2, tr1_pt3, (255, 255, 255))
            # cv2.line(img_new_face, tr1_pt1, tr1_pt3, (0, 0, 0))
            # lines_space = cv2.bitwise_and(img, img, mask=lines_space_mask)

            rect1 = cv2.boundingRect(triangle)
            (x, y, w, h) = rect1

            cropped_tr1_mask = np.zeros((h, w), np.uint8)

            points = np.array([[tr1_pt1[0] - x, tr1_pt1[1] - y],
                               [tr1_pt2[0] - x, tr1_pt2[1] - y],
                               [tr1_pt3[0] - x, tr1_pt3[1] - y]], np.int32)

            cv2.fillConvexPoly(cropped_tr1_mask, points, 255)

            # Warp triangles
            points2 = np.float32(points2)
            points = np.float32(points)
            M = cv2.getAffineTransform(points2, points)
            warped_triangle = cv2.warpAffine(cropped_triangle, M, (w, h))
            warped_triangle = cv2.bitwise_and(warped_triangle, warped_triangle, mask=cropped_tr1_mask)

            # Reconstructing destination face2
            img_new_face_rect_area = img_new_face[y: y + h, x: x + w]
            img_new_face_rect_area_gray = cv2.cvtColor(img_new_face_rect_area, cv2.COLOR_BGR2GRAY)
            _, mask_triangles_designed = cv2.threshold(img_new_face_rect_area_gray, 1, 255, cv2.THRESH_BINARY_INV)
            warped_triangle = cv2.bitwise_and(warped_triangle, warped_triangle, mask=mask_triangles_designed)

            img_new_face_rect_area = cv2.add(img_new_face_rect_area, warped_triangle)
            img_new_face[y: y + h, x: x + w] = img_new_face_rect_area
            # Lines space
            # cv2.line(img_face_mask, tr1_pt1, tr1_pt2, 0)
            # cv2.line(img_face_mask, tr1_pt2, tr1_pt3, 0)
            # cv2.line(img_face_mask, tr1_pt1, tr1_pt3, 0)
            # cv2.line(img_new_face, tr1_pt1, tr1_pt2, (0,0,0))
            # cv2.line(img_new_face, tr1_pt2, tr1_pt3, (0,0,0))
            # cv2.line(img_new_face, tr1_pt1, tr1_pt3, (0,0,0))
            # lines_space = cv2.bitwise_and(img, img, mask=lines_space_mask)
        # cv2.imwrite(os.path.join('results', "5.jpg"), img_new_face)
        # cv2.imshow("s", img_new_face)
        # cv2.waitKey(0)



        img_face_mask = cv2.bitwise_not(img_head_mask)
        img_head_noface = cv2.bitwise_and(img, img, mask=img_face_mask)
        img_new_face = cv2.medianBlur(img_new_face, 3)
        result = cv2.add(img_head_noface, img_new_face)
        # result = cv2.medianBlur(result, 3)
        # cv2.imshow("k",result)
        # cv2.waitKey(0)
        (x, y, w, h) = cv2.boundingRect(convexhull)
        center_face = (int((x + x + w) / 2), int((y + y + h) / 2))
        # cv2.imshow("a", img_head_noface)
        # cv2.imshow("b", img_head_noface)
        # cv2.imshow("d", result)
        # cv2.imshow("c", img)
        # cv2.waitKey(0)
        img = cv2.seamlessClone(result, img, img_head_mask, center_face, cv2.MIXED_CLONE)
    # img = cv2.medianBlur(img, 3)
    img = cv2.resize(img, dsize=(0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
    # cv2.imwrite(os.path.join('results', "6.jpg"), img)
    # cv2.imshow("a", img)
    # cv2.waitKey(0)
    return img

# 스티커 붙이기
'''
img : 원본 image
swap_area : pixel 처리 할 사각형 좌표
sticker : 원본 sticker
'''
def sticker_swap(img, swap_area, sticker):

    h, w, _ = img.shape
    _, _, a = sticker.shape
    for k in range(0, len(swap_area)):
        x1 = int( swap_area[k][0] - ( (swap_area[k][2]-swap_area[k][0])*0.1 ))
        y1 = int( swap_area[k][1] - ( (swap_area[k][3]-swap_area[k][1])*0.1 ))
        x2 = int( swap_area[k][2] + ( (swap_area[k][2]-swap_area[k][0])*0.1 ))
        y2 = int( swap_area[k][3] + ( (swap_area[k][3]-swap_area[k][1])*0.1 ))

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > w:
            x2 = w
        if y2 > h:
            y2 = h
        sticker_resize = cv2.resize(sticker, dsize=(x2 - x1,y2 - y1))
        if a==4 :
            for i in range(y2-y1):
                for j in range(x2-x1):
                    alpha = float(sticker_resize[i][j][3] / 255.0)
                    img[i+y1][j+x1] = alpha * sticker_resize[i][j][:3] + (1 - alpha) * img[i+y1][j+x1]
        else :
            for i in range(y2-y1):
                for j in range(x2-x1):
                    img[i+y1][j+x1] = sticker_resize[i][j][:3]

    return img