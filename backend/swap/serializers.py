from rest_framework import serializers
from .models import User, Knownface, Faces


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

class FacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faces
        fields = '__all__'

class FriendsFaceListSerializer(serializers.ModelSerializer):
    facekey = FacesSerializer(read_only=True)

    class Meta:
        model = Knownface
        fields = ('kid', 'fname', 'facekey')