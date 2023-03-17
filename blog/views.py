from django.shortcuts import render
from .models import Post

def Posts(request):
    posts = Post.objects.all()
    return render(request,'blog-masonry-2cols.html',{'posts':posts})