from nayakhabar.models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(min_length=6,write_only=True)
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','password']

    def validate(self,args):
        email=args.get("email",None)
        username=args.get("username",None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email',('Email Already Exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':('Username Already Exists')})

        return super().validate(args)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['title','summary','description','location','image','is_sticky','status','category','reporter','added_by']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields=['id','title','summary','cover_image','status','added_by']


class GalleryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=GalleryImages
        fields=['id','gallery','other_image']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields=['id','title','summary','video_link','video_id','added_by']