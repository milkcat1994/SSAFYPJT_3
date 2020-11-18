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

# for decode binary to img
import base64

#for img delete os: file del / shutil : folder del
import os,shutil


# for global variable
from django.conf import settings

IMAGES_URL = settings.IMAGES_URL

# 조회
class FriendFindViewSet(viewsets.ModelViewSet):
# class FriendFindViewSet(APIView):
    # swagger annotation
    @api_view(['GET'])
    def find_by_UID(request, uid):
        """
        uid에 해당하는 유저의 친구들 목록
        ---
            - param : uid
            - return : friend list [{kid, fname, img, uid}, ...]
        """
        knownface_list = Knownface.objects.filter(uid=uid)
        serializer = KnownfaceListSerializer(knownface_list, many=True)
        return Response(serializer.data)
       

    @api_view(['GET'])
    def find_by_KID(request, kid):
        """
        kid에 해당하는 친구 조회 (친구 상세조회)
        ---
            - param : kid
            - return : friend {kid, fname, img, uid} / 404
        """
        knownface = get_object_or_404(Knownface, kid=kid)
        serializer = KnownfaceSerializer(knownface)
        return Response(serializer.data)

    # 친구의 기타 사진들 조회
    @api_view(['GET'])
    def find_faces_by_KID(request, kid):
        """
        kid에 해당하는 친구의 등록된 얼굴들 조회
        ---
            - param : kid
            - return : face list {  main_face: {fid, img, kid},
                                    others: [{fid, img, kid}, ...]
                                }
        """
        # 대표 얼굴을 구하기 위한 friend
        friend = get_object_or_404(Knownface, kid=kid)
        main_img = friend.img
        # 대표얼굴
        main_face = get_object_or_404(Faces, img=main_img)
        main_face_serializer = FacesSerializer(main_face)
        # 대표얼굴 fid
        main_fid = main_face.fid

        # 대표 얼굴을 제외한 얼굴들
        faces = Faces.objects.filter(kid=kid).exclude(fid=main_fid)
        serializer = FacesListSerializer(faces, many=True)

        return Response({'main_face': main_face_serializer.data, 'others': serializer.data})
        # return Response(serializer.data)

    # 등록된 얼굴 상세 조회(faces)
    @api_view(['GET'])
    def find_face_by_FID(request, fid):
        """
        fid에 해당하는 친구얼굴 상세 조회
        ---
            - param : fid
            - return : face {fid, img, kid} / 404
        """
        face = get_object_or_404(Faces, fid=fid)
        serializer = FacesSerializer(face)
        return Response(serializer.data)

# 삭제
class FriendDeleteViewSet(viewsets.ModelViewSet):

    # 친구 삭제
    @api_view(['DELETE'])
    def delete_friend(request, kid):
        """
        kid에 해당하는 친구 삭제
        ---
            - param : kid, uid
            - return : {'message': 'success'} / {'message': 'fail'} / 404
        """
        if request.method == 'DELETE':
            friend = get_object_or_404(Knownface, kid=kid)

            # kid 폴더 위치 
            img_url = str(friend.uid.uid) + '/knownface/' + str(kid) + '/' 
            
            # kid 폴더 삭제 
            shutil.rmtree(IMAGES_URL+ img_url)

            friend.delete()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'fail'})

    # 친구 얼굴사진 삭제
    @api_view(['DELETE'])
    def delete_face(request, fid):
        """
        fid에 해당하는 얼굴 이미지 삭제
        ---
            - param : fid
            - return : {'message': 'success'} / {'message': 'fail'} / 404
        """
        if request.method == 'DELETE':
            face = get_object_or_404(Faces, fid=fid)
            kid = face.kid.kid
            uid = get_object_or_404(Knownface, kid=kid).uid.uid

            # 친구의 얼굴사진이 한장남았는지 확인
            faces = Faces.objects.filter(kid=face.kid)
            face_list = FacesListSerializer(faces, many=True).data
            if (len(face_list) <= 1):
                # 친구 얼굴이 모두 삭제 되면 친구를 삭제
                friend = get_object_or_404(Knownface, kid=kid)
                img_url_f = str(friend.uid.uid) + '/knownface/' + str(kid) + '/' 
                # 친구 폴더 삭제
                shutil.rmtree(IMAGES_URL+ img_url_f)
                # 친구 삭제
                friend.delete()
                return Response({'message': 'success'})
            
            

            # fid 사진파일 위치 
            img_url = str(uid) + '/knownface/' + str(kid) + '/' + str(face.fid) + ".jpg"

            # fid 사진파일 삭제 
            os.remove(IMAGES_URL+ img_url)
            # 얼굴 삭제
            face.delete()
            

            return Response({'message': 'success'})
        else:
            return Response({'message': 'fail'})


# 등록
class FriendAddViewSet(viewsets.ModelViewSet):
    # 친구 등록
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'fname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    @api_view(['POST'])
    def add_friend(request):
        """
        친구 등록
        ---
            - request body : friend(uid, fname, img)
            - return : friend {kid, fname, img, uid} / {'message': 'fail'} / 404
        """
        if request.method == 'POST':
            uid = request.data['uid']
            fname = request.data['fname']
            img = request.data['img'] #바이너리 형태의 img
           
            slice_idx = img.find("base64,") #  b의 위치
            if (slice_idx >=  0):
                img = img[slice_idx + len("base64,"):] # ,의 위치 

            # 친구 정보 저장
            user = get_object_or_404(User, uid=uid)
            # friend = Knownface(uid=user, fname=fname, img=img)
            friend = Knownface(uid=user, fname=fname)
            friend.save()

            # 얼굴 등록을 위한 kid
            kid = friend.kid
            
            # 얼굴 등록
            face = Faces(kid=friend)
            face.save()
            
            # 이미지 url 등록을 위한 fid
            fid = face.fid

            # 이미지 폴더
            img_url = uid + '/knownface/' + str(kid) + '/'
            # 디렉터리 생성
            createFolder(IMAGES_URL + img_url)
            # 이미지 url
            img_url = uid + '/knownface/' + str(kid) + '/' + str(fid) + ".jpg"

            # 저장 url ../../images/ + img_url
            # binary 를 img 로 decode 후 이미지 저장하기    
            with open(IMAGES_URL+img_url, 'wb') as f: # 결과값을 저장할 파일명.jpg or .png 도 가능
                f.write(base64.b64decode(img)) # 바이너리로된 img 를 decode 한다.
     
            # 친구 대표 이미지 등록
            friend.img = img_url
            friend.save()

            # 얼굴 등록
            face.img = img_url
            face.save()


            # return Response({'message': 'success'})
            return Response(KnownfaceSerializer(friend).data)

        return Response({'message': 'fail'})

    # 얼굴 등록
    @swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        # 'uid': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'kid': openapi.Schema(type=openapi.TYPE_INTEGER, description='int'),
        'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    @api_view(['POST'])
    def add_face(request):
        """
        친구의 얼굴 등록
        ---
            - request body : {kid, img}
            - return : face {fid, img, kid} / {'message': 'fail'} / 404
        """
        if request.method == 'POST':
            # uid = request.data['uid']
            kid = request.data['kid']
            img = request.data['img']

            slice_idx = img.find("base64,") #  b의 위치
            if (slice_idx >=  0):
                img = img[slice_idx + len("base64,"):] # ,의 위치 

            friend = get_object_or_404(Knownface, kid=kid)
            face = Faces(kid=friend)
            face.save()

            # 이미지 저장을 위한 fid, uid
            fid = face.fid
            uid = get_object_or_404(Knownface, kid=kid).uid.uid

            # 이미지 url등록 
            img_url = str(uid) + '/knownface/' + str(kid) + '/' + str(fid) + ".jpg"

            # 친구사진: uid/knownface/kid/fid.jpg
            # binary 를 img 로 decode 후 이미지 저장하기    
            with open(IMAGES_URL+img_url, 'wb') as f: # 결과값을 저장할 파일명.jpg or .png 도 가능
                f.write(base64.b64decode(img)) # 바이너리로된 img 를 decode 한다.

            # 이미지 경로 저장
            face.img = img_url
            face.save()
            
            # return Response({'message': 'success'})
            return Response(FacesSerializer(face).data)

        return Response({'message': 'fail'})


class FriendUpdateViewSet(viewsets.ModelViewSet):

    @swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'kid': openapi.Schema(type=openapi.TYPE_INTEGER, description='int'),
        'fname': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        # 'img': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        }
    ))
    @api_view(['PUT'])
    def update_friend(request):
        """
        친구 정보 수정
        ---
            - request body : {kid, fname}
            - return : friend {kid, fname, img, uid} / {'message': 'fail'} / 404
        """
        if request.method == 'PUT':
            kid = request.data['kid']
            fname = request.data['fname']
            # img = request.data['img']

            friend = get_object_or_404(Knownface, kid=kid)
            friend.fname = fname
            # friend.img = img
            friend.save()
            # return Response({'message': 'success'})
            return Response(KnownfaceSerializer(friend).data)

        return Response({'message': 'fail'})

    @swagger_auto_schema(method='put', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'kid': openapi.Schema(type=openapi.TYPE_INTEGER, description='int'),
        'fid': openapi.Schema(type=openapi.TYPE_INTEGER, description='int'),
        }
    ))
    @api_view(['PUT'])
    def update_friend_img(request):
        """
        친구 대표이미지 수정
        ---
            - request body : {kid, fid}  변경하려는 친구의 kid, 대표사진으로 설정할fid
            - return : friend {kid, fname, img, uid} / {'message': 'fail'} / 404
        """
        if request.method == 'PUT':
            kid = request.data['kid']
            fid = request.data['fid']

            # 변경할 대표사진 
            face = get_object_or_404(Faces, fid=fid)
            img = face.img            
            
            # 친구의 대표 이미지 변경
            friend = get_object_or_404(Knownface, kid = kid)
            friend.img = img
            friend.save()
            return Response(KnownfaceSerializer(friend).data)

        return Response({'message': 'fail'})


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)