from rest_framework import serializers
from .models import Sticker

class StickerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = '__all__'

class StickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sticker
        fields = '__all__'