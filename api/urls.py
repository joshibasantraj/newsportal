from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router=DefaultRouter()

router.register('categoryapi',views.CategoryViewSet,basename='categoryapi')
router.register('newsapi',views.NewsViewSet,basename='newsapi')
router.register('galleryapi',views.GalleryViewSet,basename='galleryapi')
router.register('galleryimagesapi',views.GalleryImagesViewSet,basename='galleryimagesapi')
router.register('videoapi',views.VideoViewSet,basename='videoapi')


urlpatterns = [
    path('',include(router.urls)),
    path('register-user/',views.UserRegistration.as_view(),name="register"),
    path('token-obtain/',TokenObtainPairView.as_view(),name="token-obtain"),
    path('token-refresh/',TokenRefreshView.as_view(),name="token-refresh"),
    path('token-verify/',TokenVerifyView.as_view(),name="token-verify"),
]
