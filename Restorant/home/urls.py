from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.sign,name='sign'),
    path('loginp',views.loginp,name='loginp'),
    # path('loginp',views.logoutuser,name="logout"),
    
    path('index',views.index,name='index'),
    path('about', views.about,name='about'),
    path('services', views.services ,name='services'),
    path('contact', views.contact, name='contact'),
    path('courses', views.courses, name='courses'),
    path('kaushik',views.kaushik,name='kaushik')
]