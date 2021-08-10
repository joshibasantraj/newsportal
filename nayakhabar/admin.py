from django.contrib import admin
from .models import Category,News,Gallery,GalleryImages,Video,Reporter

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','summary','status','image','added_by']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','summary','description','location','image','news_date','is_sticky','status','image','category','reporter','added_by']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display=['title','summary','status','cover_image','added_by']

@admin.register(GalleryImages)
class GalleryImagesAdmin(admin.ModelAdmin):
    list_display=['gallery','other_image']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display=['title','summary','video_link','video_id','added_by']

@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    list_display=['user','address','joined_date']