"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url 
from rest_framework import permissions

# for swagger
from django.conf.urls import url 
from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

schema_url_patterns = [ 
    path('friends/', include('friends.urls')), 
    path('sticker/', include('sticker.urls')), 
    path('user/', include('user.urls')),
    path('swap/', include('swap.urls')),
] 

schema_view = get_schema_view( 
    openapi.Info( 
        title="Django API", 
        default_version='v1', 
        terms_of_service="https://www.google.com/policies/terms/", 
    ), 
    public=True, 
    permission_classes=(permissions.AllowAny,), 
    patterns=schema_url_patterns, 
)


urlpatterns = [
    # for swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # # 관리자
    # path('admin/', admin.site.urls),
    # 친구 관련 기능
    path('friends/', include('friends.urls')),
    # 스티커 관련 기능
    path('sticker/', include('sticker.urls')),
    path('user/', include('user.urls')),
    # 이미지 업로드 및 결과사진 반환
    path('swap/', include('swap.urls')),
]
