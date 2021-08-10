from nayakhabar.models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import uuid
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate,login,logout

class UserRegistration(CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            if user is not None:
                login(self.request,user)
            return Response({
                "Request-Id":str(uuid.uuid4()),
                "Message":"User Created Successfully",
                "User":serializer.data,
            },status=status.HTTP_201_CREATED)
        return Response({"Errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]

class NewsViewSet(viewsets.ModelViewSet):
    queryset=News.objects.all()
    serializer_class=NewsSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class GalleryViewSet(viewsets.ModelViewSet):
    queryset=Gallery.objects.all()
    serializer_class=GallerySerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class GalleryImagesViewSet(viewsets.ModelViewSet):
    queryset=GalleryImages.objects.all()
    serializer_class=GalleryImagesSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

class VideoViewSet(viewsets.ModelViewSet):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]