# from django.http import HttpResponse
# , JsonResponse

from django.shortcuts import get_object_or_404

from .models import User, Sticker
from .serializers import StickerSerializer, StickerListSerializer

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# for swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# for remove file
import os
import base64

# class IndexViewSet(viewsets.ModelViewSet):
#     def index(self):
#         return HttpResponse("sticker app")

# for global variable
from django.conf import settings

IMAGES_URL = settings.IMAGES_URL

# 조회
class StickerFindViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def find_all_sticker(request):
        """
        기본 스티커 조회
        ---
            - param : None
            - return : sticker list [{sid, img, uid}, ...]
        """
        sticker_list = Sticker.objects.filter(uid="bc3a81c4-29d0-402e-9ef2-7c19396bd6b2")
        serializer = StickerListSerializer(sticker_list, many=True)
        return Response(serializer.data)


    # swagger annotation
    @api_view(['GET'])
    def find_by_UID(request, uid):
        """
        uid로 등록한 스티커 목록
        ---
            - param : uid
            - return : sticker list [{sid, img, uid}, ...]
        """
        sticker_list = Sticker.objects.filter(uid=uid)
        serializer = StickerListSerializer(sticker_list, many=True)
        return Response(serializer.data)
      
    @api_view(['GET'])
    def find_by_SID(request, sid):
        """
        sid에 해당하는 스티커 조회 (스티커 상세조회)
        ---
            - param : sid
            - return : sticker {sid, img, uid} / 404
        """
        sticker = get_object_or_404(Sticker, sid=sid)
        serializer = StickerSerializer(sticker)
        return Response(serializer.data)

# 삭제
class StickerDeleteViewSet(viewsets.ModelViewSet):

    # 스티커 삭제
    @api_view(['DELETE'])
    def delete_sticker(request, sid):
        """
        sid에 해당하는 스티커 삭제
        ---
            - param : sid
            - return : {'message': 'success'} / {'message': 'fail'} / 404
        """
        if request.method == 'DELETE':
            sticker = get_object_or_404(Sticker, sid=sid)
            uid = sticker.uid.uid

            # 기본 스티커 삭제 불가
            if str(uid) == "bc3a81c4-29d0-402e-9ef2-7c19396bd6b2":
                return Response({'message': 'fail'})

            img_url = sticker.img
            os.remove(IMAGES_URL + img_url)

            sticker.delete()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'fail'})


# 등록
class StickerAddViewSet(viewsets.ModelViewSet):
    # 스티커 등록
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        # 'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    @api_view(['POST'])
    def add_sticker(request):
        """
        스티커 등록
        ---
            - request body : {uid,  img} * 필수값, nullx, ""로주세요
            - return : sticker {sid,  img, uid} / {'message': 'fail'} / 404
        """
        if request.method == 'POST':
            uid = request.data['uid']
            # name = request.data['name']
            img = request.data['img']

            slice_idx = img.find("base64,") #  b의 위치
            if (slice_idx >=  0):
                img = img[slice_idx + len("base64,"):] # ,의 위치 

            user = get_object_or_404(User, uid=uid)
            # sticker = Sticker(uid=user, name=name, img=img)
            # sticker = Sticker(uid=user, name=name)
            sticker = Sticker(uid=user)
            sticker.save()

            # 스티커 저장을 위한 sid
            sid = sticker.sid

            # 저장 url
            img_url = str(uid) + '/sticker/' + str(sid) + ".jpg"
            createFolder(IMAGES_URL + str(uid) + '/sticker/')

            # 이미지 디코드 및 저장
            with open(IMAGES_URL + img_url, 'wb') as f:
                f.write(base64.b64decode(img))

            # 이미지 url저장
            sticker.img = img_url
            sticker.save()

            # return Response({'message': 'success'})
            return Response(StickerSerializer(sticker).data)

        return Response({'message': 'fail'})

# class StickerUpdateViewSet(viewsets.ModelViewSet):

#     @swagger_auto_schema(method='put', request_body=openapi.Schema(
#     type=openapi.TYPE_OBJECT, 
#     properties={
#         'sid': openapi.Schema(type=openapi.TYPE_INTEGER, description='int'),
#         # 'name': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         # 'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
#         }
#     ))
#     @api_view(['PUT'])
#     def update_sticker(request):
#         """
#         스티커 정보 수정
#         ---
#             - request body : sticker(sid, name)
#             - return : sticker {sid, name, img, uid} / {'message': 'fail'} / 404
#         """
#         if request.method == 'PUT':
#             sid = request.data['sid']
#             name = request.data['name']

#             sticker = get_object_or_404(Sticker, sid=sid)
#             sticker.name = name
#             # sticker.img = img
#             sticker.save()
#             # return Response({'message': 'success'})
#             return Response(StickerSerializer(sticker).data)

#         return Response({'message': 'fail'})
        

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)