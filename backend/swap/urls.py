from django.urls import path
from . import views

urlpatterns = [
    # path('', views.IndexViewSet.index),
    path('upload/', views.UploadImgViewSet.recog_face),
    path('result/', views.ResultImgViewSet.get_resimg),
]