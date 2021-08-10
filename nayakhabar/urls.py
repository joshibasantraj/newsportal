from django.urls import path
from . import views

urlpatterns=[
    path('admin-login/',views.AdminLogin.as_view(),name="admin-login"),
    path('admin-logout/',views.AdminLogout.as_view(),name="admin-logout"),


    path('category-list/',views.CategoryList.as_view(),name="category-list"),
    path('category-create/',views.CategoryCreate.as_view(),name="category-create"),
    path('category-update/<int:pk>/',views.CategoryUpdate.as_view(),name="category-update"),
    path('category-delete/<int:pk>/',views.CategoryDelete.as_view(),name="category-delete"),

    path('news-list/',views.NewsList.as_view(),name="news-list"),
    path('news-create/',views.NewsCreate.as_view(),name="news-create"),
    path('news-update/<int:pk>/',views.NewsUpdate.as_view(),name="news-update"),
    path('news-delete/<int:pk>/',views.NewsDelete.as_view(),name="news-delete"),

    path('gallery-list/',views.GalleryList.as_view(),name="gallery-list"),
    path('gallery-create/',views.GalleryCreate.as_view(),name="gallery-create"),
    path('gallery-update/<int:pk>/',views.GalleryUpdate.as_view(),name="gallery-update"),
    path('gallery-delete/<int:pk>/',views.GalleryDelete.as_view(),name="gallery-delete"),

    path('video-list/',views.VideoList.as_view(),name="video-list"),
    path('video-create/',views.VideoCreate.as_view(),name="video-create"),
    path('video-update/<int:pk>/',views.VideoUpdate.as_view(),name="video-update"),
    path('video-delete/<int:pk>/',views.VideoDelete.as_view(),name="video-delete"),



    ############################Front End#########################

    path('',views.HomeView.as_view(),name="home"),
    path('news-list/<int:id>/',views.CatNews.as_view(),name="catnews"),
    path('news-details/<int:id>/',views.NewsDetail.as_view(),name="newsdetail"),
]