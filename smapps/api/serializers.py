from rest_framework import serializers
from ..models import *
from rest_framework.serializers import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Post
        fields = '__all__' 

        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields = '__all__' 


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Like
        fields = '__all__' 

        
class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comments
        fields=('__all__')

class Friend_requestSerializer(ModelSerializer):
    class Meta:
        model=Friends
        fields=('__all__')