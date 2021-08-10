from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reporter(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=40,blank=True,null=True)
    joined_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title=models.CharField(max_length=50)
    summary=models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(max_length=20,choices=[('Active','Active'),('In Active','In Active')])
    image=models.ImageField(upload_to="categories",blank=True,null=True)
    added_by=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
            return self.title

    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.storage.delete(self.image.name)
        return super().delete(using=using, keep_parents=keep_parents)


    def save(self,*args,**kwargs):
        try:
            this=Category.objects.get(id=self.id)       
            if this.image!=self.image:
                this.image.delete()
        except:
                pass
        return super(Category,self).save(*args,**kwargs)
    
class News(models.Model):
    title=models.CharField(max_length=50)
    summary=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    location=models.CharField(max_length=50)
    image=models.ImageField(upload_to="news")
    news_date=models.DateTimeField(auto_now_add=True)
    is_sticky=models.BooleanField(default=False)
    status=models.CharField(max_length=50,choices=[('Published','Published'),('Un Published','Un Published')])
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    reporter=models.ForeignKey(Reporter,on_delete=models.SET_NULL,null=True)
    added_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        if self.image:
            self.image.storage.delete(self.image.name)
        return super().delete(using=using, keep_parents=keep_parents)


    def save(self,*args,**kwargs):
        try:
            this=News.objects.get(id=self.id)
            if this.image!=self.image:
                this.image.delete()
        except:
                pass
        return super(News,self).save(*args,**kwargs)



class Gallery(models.Model):
    title=models.CharField(max_length=50)
    summary=models.CharField(max_length=100)
    cover_image=models.ImageField(upload_to="gallery")
    status=models.CharField(max_length=30,choices=[('Active','Active'),('In Active','In Active')])
    added_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    
    def delete(self, using=None, keep_parents=False):
        if self.cover_image:
            other_images=GalleryImages.objects.filter(gallery=self.id).all()
            if other_images:
                for image in other_images:
                    image.other_image.storage.delete(image.other_image.name)
            self.cover_image.storage.delete(self.cover_image.name)
        return super().delete(using=using, keep_parents=keep_parents)

    def save(self,*args,**kwargs):
        try:
            this=Gallery.objects.get(id=self.id)
            if this.cover_image!=self.cover_image:
                this.cover_image.delete()
        except:
                pass
        return super(Gallery,self).save(*args,**kwargs)



    

class GalleryImages(models.Model):
    gallery=models.ForeignKey(Gallery,on_delete=models.CASCADE)
    other_image=models.ImageField(upload_to="galleryimages")

class Video(models.Model):
    title=models.CharField(max_length=50)
    summary=models.CharField(max_length=100)
    video_link=models.URLField()
    video_id=models.CharField(max_length=50)
    added_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

