from django.urls import path
from . import views

urlpatterns = [
    # path('', views.IndexViewSet.index),
    # 스티커 조회
    path('all/', views.StickerFindViewSet.find_all_sticker),
    path('<uuid:uid>/', views.StickerFindViewSet.find_by_UID),
    # 스티커 상세조회
    path('detail/<int:sid>/', views.StickerFindViewSet.find_by_SID),
    # 스티커 삭제
    path('delete/<int:sid>/', views.StickerDeleteViewSet.delete_sticker),
    # 스티커 등록
    path('add/', views.StickerAddViewSet.add_sticker),
    # 스티커 수정
    # path('update/', views.StickerUpdateViewSet.update_sticker),

]
