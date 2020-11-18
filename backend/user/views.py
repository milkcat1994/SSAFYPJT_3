from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404

from .models import User, Faces
from .serializers import UserListSerializer, UserSerializer


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import uuid
import os
import shutil

# views.py 는 데이터를 주고 받을 수 있도록 해준다. 
"""
모든 유저 조회 : find_all()
로그인 or 회원가입 : login()
유저 삭제 : delete()
유저 수정 : update()
"""
# for global variable
from django.conf import settings

IMAGES_URL = settings.IMAGES_URL

class UserAddViewSet(viewsets.ModelViewSet):
    
    # 유저 
    # 정보 존재 o : 로그인 (이메일로 유저정보 가져오기 및 domain내용 갱신)
    # 정보 존재 x : 회원가입 (이메일로 uid 생성 및 uid,email,domain 값 등록)
   
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='1234@naver.com'),
        'domain': openapi.Schema(type=openapi.TYPE_STRING, description='kakao'),
        }
    ))
    @api_view(['POST'])
    def login(request): 
        """
        uid에 해당하는 유저 조회
        도메인은 수정하고 , id 를 반환해준다. 
        ---
            - param : {  "email": "1234@naver.com","domain": "kakao"}
            - return : user
        """
        print(IMAGES_URL)
        email = request.data['email']
        domain = request.data['domain']
        try: # 로그인 정보가 있다. -> domain 수정 -> 로그인 정보반환 
            user = User.objects.get(email=email)
            user.domain = domain   # 도메인을 수정해서 저장한다. kakao or google  
        except:   # 로그인 정보가 없다. -> 유저 등록 -> 로그인 정보 반환
            user = User(uid=uuid.uuid4(),email=email, domain=domain,blur=1,pixel=1)
            uid = user.uid
            # 스티커, 업로드 이미지 사진 저장할 폴더 생성
            createFolder(IMAGES_URL + str(uid) + '/sticker/')
            createFolder(IMAGES_URL + str(uid) + '/swap/')
        
        user.save()
        return Response(UserListSerializer(user).data)


class UserViewSet(viewsets.ModelViewSet):
    # 모든 유저 조회 
    @api_view(['GET'])
    def find_all(self):
        """
        모든 유저 조회
        ---
            - param : null
            - return : users
        """
        queryset = User.objects.all()
        serializer_class = UserListSerializer(queryset, many=True)
        return Response(serializer_class.data)

    # 유저 삭제
    @api_view(['DELETE'])
    def delete(request, uid):
        """
        uid에 해당하는  유저 삭제
        ---
            - param : uid
            - return : {'message': 'success'} / {'message': 'fail'} / 404
        """
        if request.method == 'DELETE':
            user = get_object_or_404(User, uid=uid)
            # uid 의 폴더 삭제
            deleteFolder(IMAGES_URL + str(uid))
            user.delete()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'fail'})
    
# 유저 pixel, blur 값 수정 ( 값 조회는 login 으로 하면 됩니다!) 
class UserUpdateViewSet(viewsets.ModelViewSet):
    @swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'pixel': openapi.Schema(type=openapi.TYPE_INTEGER, description=1),
        'blur': openapi.Schema(type=openapi.TYPE_INTEGER, description=1),
        }
    ))
    @api_view(['PUT'])
    def update(request):
        """
        pixel,blur 정보 수정
        ---
            - request body : pixel,blur  ex) put 누르면 수정됩니다.
            - return : user / {'message': 'fail'} / 404
        """
        if request.method == 'PUT':
            uid = request.data['uid']
            pixel = request.data['pixel']
            blur = request.data['blur']
  
            # 유저의 대표 이미지 변경
            user = get_object_or_404(User, uid = uid)
            user.pixel = pixel
            user.blur = blur
            user.save()
            return Response(UserSerializer(user).data)

        return Response({'message': 'fail'})


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
def deleteFolder(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
    except OSError:
        print ('Error: Deleting directory. ' +  directory)
  


