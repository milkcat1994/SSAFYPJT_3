from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserViewSet,UserAddViewSet,UserUpdateViewSet
from .models import User

urlpatterns = [
    
    # 모든 유저 조회 
    path('all/', UserViewSet.find_all),
    # 로그인
    # 정보 존재 o : 로그인 (이메일로 유저정보 가져오기 및 domain내용 갱신)
    # 정보 존재 x : 회원가입 (이메일로 uid 생성 및 uid,email,domain 값 등록)
    path('login/', UserAddViewSet.login),
    # 유저 pixel,blur값 수정 
    path('update/', UserUpdateViewSet.update),
    # 유저 삭제
    path('delete/<uuid:uid>/', UserViewSet.delete),
    

]
