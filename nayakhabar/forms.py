from django import forms
from .models import *
from django.contrib.auth.models import User

class AdminLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['title','summary','status','image','added_by']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'added_by':forms.Select(attrs={'class':'form-control'}),
        }

        error_messages={
            'title':{
                'required':'Title field is required'
            },
            'summary':{
                'required':'Summary field is required'
            }
        }

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['title','summary','description','location','image','is_sticky','status','category','reporter','added_by']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'is_sticky':forms.CheckboxInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'reporter':forms.Select(attrs={'class':'form-control'}),
            'added_by':forms.Select(attrs={'class':'form-control'}),
            

        }

        error_messages={
            'image':{
                'required':"Image field is required"
            }
        }


class GalleryForm(forms.ModelForm):
    other_images=forms.FileField(required=False,widget=forms.FileInput(attrs={'class':'form-class','multiple':True}))
    class Meta:
        model=Gallery
        fields=['title','summary','cover_image','status','added_by','other_images']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
            'cover_image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'added_by':forms.Select(attrs={'class':'form-control'}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['title','summary','video_link','video_id','added_by']

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
            'video_link':forms.URLInput(attrs={'class':'form-control'}),
            'video_id':forms.TextInput(attrs={'class':'form-control'}),
            'added_by':forms.Select(attrs={'class':'form-control'}),
        }