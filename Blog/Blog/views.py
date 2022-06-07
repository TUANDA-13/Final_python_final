from django.shortcuts import render 
from django.urls import path
from app.models import *

def BASE(request):
    return render(request,'base.html')

def INDEX(request):
    trending_post = Post.objects.filter(section ='Trending').order_by('date')[0:4]
    popular_post = Post.objects.filter(section ='Popular').order_by('date')[0:5]
    topic = Category.objects.all()
    context ={
        'trending_post':trending_post,
        'popular_post':popular_post,
        'topic':topic,
    }
    return render(request,'index.html',context)


