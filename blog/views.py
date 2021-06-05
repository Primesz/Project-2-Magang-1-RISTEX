from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'judul':'blog'
    }
    return render(request,'blog.html',context)