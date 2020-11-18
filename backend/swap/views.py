# from django.http import HttpResponse
# , JsonResponse

from django.shortcuts import get_object_or_404

from .models import User, Knownface, Faces
from .serializers import KnownfaceListSerializer, KnownfaceSerializer, FacesListSerializer, FacesSerializer

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# for swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# for img processing
import cv2
import base64
import uuid
import numpy as np

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util import FaceController as fc

# for global variable
from django.conf import settings

IMAGES_URL = settings.IMAGES_URL
# IMAGES_URL_ABS = "/home/ubuntu/images/"

# 원본 이미지 받기. 원본 이미지를 받으면 친구 및 친구 얼굴들이 조회되어야함.
class UploadImgViewSet(viewsets.ModelViewSet):
    # swagger annotation
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    @api_view(['POST'])
    def recog_face(request):
        """
        이미지를 받아서 인식된 얼굴 정보 반환
        ---
            - param : {uid: "String", img: "String"}  비회원은 uid: ""
            - return : {"friend_list": friend_list(인식된친구),"faces_area": faces_area(좌표), "faces_crop": faces_crop(b64encoded),}
        """
        if request.method == 'POST':
            uid = request.data['uid']
            img = request.data['img']

            slice_idx = img.find("base64,") #  b의 위치
            if (slice_idx >=  0):
                img = img[slice_idx + len("base64,"):] # ,의 위치 

            # 회원일 경우
            if uid != "":   
                # 친구들 리스트
                Knownfaces = Knownface.objects.filter(uid=uid)
                serializer = KnownfaceListSerializer(Knownfaces, many=True)
                # 2번째 인자
                friends = serializer.data
                

            # 비회원일 경우 친구가 없음
            if uid == "":
                # 비회원일 경우 임시 uid생성
                # uid = uuid.uuid4()
                friends = []


            # encode: img -> binary
            # base64 디코딩
            ################# test부분 ###################
            # img_sample = os.path.dirname( os.path.abspath( __file__ ) ).replace("\\","/") + '/april.jpg'

            # img= ""
            # with open(img_sample, 'rb') as single_img: # binary로 변경할 파일명.jpg
            #     img = base64.b64encode(single_img.read())  #  img 를 바이너리로 encode 한다.
            ##############################################

            # 친구 crop된 사진들 base64로 엔코딩해서 리스트로 보내주기
            # base64 decode -> cv2 decode
            # img 저거 자르기

            decoded_data = base64.b64decode(img)
            np_data = np.fromstring(decoded_data,np.uint8)
            img_cv2 = cv2.imdecode(np_data,cv2.IMREAD_COLOR)

            faces_area, faces_crop, friend_list = fc.face_detection(img_cv2, friends)

            # recog_img_url, 얼굴 좌표값 리턴 
            # return Response({'img': recog_img_url, 'face_pos': face_pos})
            # print(faces_crop[0])
            
            return Response({"friend_list": friend_list,"faces_area": faces_area, "faces_crop": faces_crop,})

        return Response({'message': 'fail'})

class ResultImgViewSet(viewsets.ModelViewSet):

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'), # string (base64)
        'optionType': openapi.Schema(type=openapi.TYPE_STRING, description='string'), # ['blur', 'pixel' , 'swap','sticker']
        'optionlevel': openapi.Schema(type=openapi.TYPE_INTEGER, description=1), # pixel , blur의 강도 [1, 2, 3, 4, 5] 중 하나
        'sticker': openapi.Schema(type=openapi.TYPE_STRING, description='string'), # 선택된 스티커 사진 string (base64) 
        'targetFace': openapi.Schema(type=openapi.TYPE_ARRAY, items='object', description='array') # 수정할 얼굴의 좌표배열 [[x1,y1,x2,y2],[x1,y1,x2,y2],...]
        }
    ))
    @api_view(['POST'])
    def get_resimg(request):
        """
        변환 타입(blur, pixel,swap,sticker) 과 선택된 얼굴정보 받아서 결과 이미지 반환
        ---
            - param : {
                        img: String(base64), 
                        optionType: ['blur', 'pixel', 'swap', 'sticker'],
                        optionlevel: [1, 2, 3, 4, 5],
                        sticker : String(base64) ,
                        targetFace :[[x1,y1,x2,y2],[x1,y1,x2,y2],...]
                      }
            - return : {img}
        """

        if request.method == 'POST':
            
            img = request.data['img']
            optionType = request.data['optionType']
            optionlevel = request.data['optionlevel']
            sticker = request.data['sticker']
            targetFace = request.data['targetFace']

            ################# test부분 ###################
            # img_sample = os.path.dirname(os.path.abspath( __file__ ) ).replace("\\","/") + '/april.jpg'
            # # img_sample ="/redvelvet.jpg"
            # with open(img_sample, 'rb') as single_img: # binary로 변경할 파일명.jpg
            #     img = base64.b64encode(single_img.read())  #  img 를 바이너리로 encode 한다.
            
            # optionType ="blur"
            # optionlevel = 1
            # sticker_sample = os.path.dirname(os.path.abspath( __file__ )).replace("\\","/") + '/smith.png'
            # with open(sticker_sample, 'rb') as single_img: # binary로 변경할 파일명.jpg
            #     sticker = base64.b64encode(single_img.read())  #  sticker 를 바이너리로 encode 한다.
            # targetFace =[(185, 41, 223, 79),  (218, 43, 260, 85), (85, 44, 128, 87), (47, 56, 92, 101)]
            # targetFace =[(185, 41, 223, 79), (133, 36, 175, 78), (218, 43, 260, 85), (85, 44, 128, 87), (47, 56, 92, 101)]
            ##############################################
            
            optionlevel = 6 - optionlevel

            slice_idx = img.find("base64,") #  b의 위치
            if (slice_idx >=  0):
                img = img[slice_idx + len("base64,"):] # ,의 위치 

            if optionType == 'sticker':
                slice_idx = sticker.find("base64,") #  b의 위치
                if (slice_idx >=  0):
                    sticker = sticker[slice_idx + len("base64,"):] # ,의 위치 

        # base64 decode -> cv2 decode
            # img 사진 cv2로 decode하기
            decoded_data = base64.b64decode(img)
            np_data = np.fromstring(decoded_data,np.uint8)
            img_cv2 = cv2.imdecode(np_data,cv2.IMREAD_COLOR)
            
            # sticker 사진 cv2로 decode하기
            if optionType == 'sticker':
                decoded_data = base64.b64decode(sticker)
                np_data = np.fromstring(decoded_data,np.uint8)
                sticker = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
            
            # blur ,pixel, swap, sticker 처리
            ch_img =fc.face_transform(optionType, img_cv2, targetFace, optionlevel, sticker)
            
            ################# test부분 ###################
            # with open(os.path.dirname(os.path.abspath( __file__ )).replace("\\","/") + '/april_blur-lv1.jpg', 'wb') as f: # 결과값을 저장할 파일명.jpg
                # f.write(base64.b64decode(ch_img)) # 바이너리로된 img 를 decode 한다
            ##############################################
            
            # cv2.imshow('',ch_img)

            # 결과사진 url 리턴
            return Response({'img': ch_img})

        return Response({'message': 'fail'})
