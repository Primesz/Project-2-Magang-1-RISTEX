from django.shortcuts import render
<<<<<<< HEAD
from .models import Blog
# Create your views here.
def blog_index(request):
    blogs = Blog.objects.all()
    context = {
    'blogs': blogs
    }
    return render(request, 'blog_index.html', context)
def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
    'blog': blog
    }
    return render(request, 'blog_detail.html', context)
=======

# Create your views here.
def index(request):
    context={
        'judul':'blog'
    }
    return render(request,'blog.html',context)
>>>>>>> 547a2971384fd6ae1acd61238effeaee58ae52c4
