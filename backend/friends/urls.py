from django.urls import path
from . import views

urlpatterns = [
    # path('', views.IndexViewSet.index),
    # 친구 목록 조회
    path('<uuid:uid>/', views.FriendFindViewSet.find_by_UID),
    # path('', views.FriendViewSet.find_by_UID),
    # 친구 상세조회
    path('detail/<int:kid>/', views.FriendFindViewSet.find_by_KID),
    path('detail/faces/<int:kid>/', views.FriendFindViewSet.find_faces_by_KID),
    # 얼굴 상세 조뢰
    path('detail/face/<int:fid>/', views.FriendFindViewSet.find_face_by_FID),
    # 친구 삭제
    path('delete/<int:kid>/', views.FriendDeleteViewSet.delete_friend),
    # 친구 얼굴 삭제
    path('delete/face/<int:fid>/', views.FriendDeleteViewSet.delete_face),
    # 친구 등록
    path('add/', views.FriendAddViewSet.add_friend),
    # 얼굴 등록
    path('add/face/', views.FriendAddViewSet.add_face),
    # 친구 수정
    path('update/', views.FriendUpdateViewSet.update_friend),
    # 친구 대표사진 수정
    path('update/img/', views.FriendUpdateViewSet.update_friend_img),

]
