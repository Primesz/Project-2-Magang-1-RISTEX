from django.urls import path
from . import views
<<<<<<< HEAD
urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
=======

urlpatterns = [
    path('',views.index)
>>>>>>> 547a2971384fd6ae1acd61238effeaee58ae52c4
]