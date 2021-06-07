from django.shortcuts import render

# Create your views here.

def KalkulatorKesehatan(request):
    context={
        'judul':'profil'
    }
    return render(request,'profil.html',context)

# Janlup diganti

