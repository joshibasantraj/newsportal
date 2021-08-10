from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,TemplateView,FormView,View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

# Create your views here.
class AdminMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and request.user.is_staff==1:
            pass
        else:
            return redirect("admin-login")
        return super().dispatch(request, *args, **kwargs)

class AdminLogout(View):
    def get(self,request):
        logout(self.request)
        return redirect("admin-login")

class AdminLogin(FormView):
    template_name="useradmin/admin-login.html"
    form_class=AdminLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff==1:
            return HttpResponseRedirect('/category-list/')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        uname=form.cleaned_data["username"]
        psw=form.cleaned_data["password"]
        user=authenticate(username=uname,password=psw)
        if user is not None and user.is_staff==1:
            login(self.request,user)
            return HttpResponseRedirect("/category-list/")
        return super().form_valid(form)
    


class CategoryList(AdminMixin,ListView):
    model=Category
    template_name="useradmin/category/index.html"
    context_object_name="categories"

class CategoryCreate(AdminMixin,CreateView):
    template_name="useradmin/category/form.html"
    success_url=reverse_lazy("category-list")
    form_class=CategoryForm

    def form_valid(self, form):
        messages.success(self.request,"Category Created Successfully")
        return super().form_valid(form)

class CategoryUpdate(AdminMixin,UpdateView):
    model=Category
    template_name="useradmin/category/form.html"
    success_url=reverse_lazy("category-list")
    form_class=CategoryForm

    def form_valid(self, form):
        messages.success(self.request,"Category Updated Successfully")
        return super().form_valid(form)

class CategoryDelete(AdminMixin,DeleteView):
    model=Category
    success_url=reverse_lazy("category-list")

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"Category Deleted Successfully")
        return super().post(request, *args, **kwargs)



class NewsList(AdminMixin,ListView):
    model=News
    template_name="useradmin/news/index.html"


class NewsCreate(AdminMixin,CreateView):
    template_name="useradmin/news/form.html"
    success_url=reverse_lazy("news-list")
    form_class=NewsForm

    def form_valid(self, form):
        messages.success(self.request,"News Created Successfully")
        return super().form_valid(form)

class NewsUpdate(AdminMixin,UpdateView):
    model=News
    template_name="useradmin/news/form.html"
    success_url=reverse_lazy("news-list")
    form_class=NewsForm

    def form_valid(self, form):
        messages.success(self.request,"News Updated Successfully")
        return super().form_valid(form)

class NewsDelete(AdminMixin,DeleteView):
    model=News
    success_url=reverse_lazy("news-list")

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"News Deleted Successfully")
        return super().post(request, *args, **kwargs)


class GalleryList(AdminMixin,ListView):
    model=Gallery
    template_name="useradmin/gallery/index.html"


class GalleryCreate(AdminMixin,CreateView):
    template_name="useradmin/gallery/form.html"
    success_url=reverse_lazy("gallery-list")
    form_class=GalleryForm

    def form_valid(self, form):
        fm=form.save()
        messages.success(self.request,"Gallery Created Successfully")
        more_images=self.request.FILES.getlist("other_images")
        if more_images:
            for image in more_images:
                GalleryImages.objects.create(gallery=fm,other_image=image)
        
        return super().form_valid(form)

class GalleryUpdate(AdminMixin,UpdateView):
    model=Gallery
    template_name="useradmin/gallery/form.html"
    success_url=reverse_lazy("gallery-list")
    form_class=GalleryForm

    def form_valid(self, form):
        fm=form.save()
        messages.success(self.request,"Gallery Updated Successfully")
        more_images=self.request.FILES.getlist("other_images")
        if more_images:
            for image in more_images:
                GalleryImages.objects.create(gallery=fm,other_image=image)
        return super().form_valid(form)

class GalleryDelete(AdminMixin,DeleteView):
    model=Gallery
    success_url=reverse_lazy("gallery-list")

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"Gallery Deleted Successfully")
        return super().post(request, *args, **kwargs)



class VideoList(AdminMixin,ListView):
    model=Video
    template_name="useradmin/video/index.html"


class VideoCreate(AdminMixin,CreateView):
    template_name="useradmin/video/form.html"
    success_url=reverse_lazy("video-list")
    form_class=VideoForm

    def form_valid(self, form):
        fm=form.save()
        messages.success(self.request,"video Created Successfully")  
        return super().form_valid(form)

class VideoUpdate(AdminMixin,UpdateView):
    model=Video
    template_name="useradmin/video/form.html"
    success_url=reverse_lazy("video-list")
    form_class=VideoForm

    def form_valid(self, form):
        fm=form.save()
        messages.success(self.request,"Video Updated Successfully")
        return super().form_valid(form)

class VideoDelete(AdminMixin,DeleteView):
    model=Video
    success_url=reverse_lazy("video-list")

    def post(self, request, *args, **kwargs):
        messages.success(self.request,"video Deleted Successfully")
        return super().post(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name="frontend/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["bignews"]=News.objects.filter(is_sticky=1).first()
        context["videos"]=Video.objects.all()
        context["gallery"]=Gallery.objects.all()
        return context


class CatNews(TemplateView):
    template_name="frontend/inner.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        cat_id=self.kwargs['id']
        news=News.objects.filter(category=cat_id).all()
        context["cat_id"]=cat_id
        context['news']=news
        context["categories"] = Category.objects.all()
        return context
    
class NewsDetail(TemplateView):
    template_name="frontend/news.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        news_id=self.kwargs['id']
        news=News.objects.get(id=news_id)
        cat_id=news.category.id
        context['cat_id']=cat_id
        context['related_news']=News.objects.filter(category=cat_id).all()
        context['news']=news
        context["categories"] = Category.objects.all()
        return context

