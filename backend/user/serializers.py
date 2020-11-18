from rest_framework import serializers
from .models import User, Knownface, Sticker, Faces

# serializer.py는 데이터를 보여주는 역할을 한다. 

class KnownfaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knownface
        fields = '__all__'


class KnownfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Knownface
        fields = '__all__'

class FacesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faces
        fields = '__all__'

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'