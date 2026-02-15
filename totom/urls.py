
from django.contrib import admin
from django.urls import path
from app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('about-totom/', views.konaba, name="konaba"),
    path('totom-members/', views.membru, name="membru"),
]
