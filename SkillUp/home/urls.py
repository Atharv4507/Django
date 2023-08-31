from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views
# from django_registration.backends.activation.views import RegistrationView
# from yourapp.forms import RegistrationWithNameForm
urlpatterns = [
    path('',views.sign,name='sign'),
    path('loginp',views.loginp,name='loginp'),
    path('index',views.index,name='home'),
    path('about', views.about,name='about'),
    path('services', views.services ,name='services'),
    path('contact', views.contact, name='contact'),
    path('profile',views.profile,name='profile'),
    path('pl', views.pl, name='pl'),
    path('lang', views.lang,name='lang'),
    # path('pythonb', views.pythonb,name='pythonb'),
    path('py1intro', views.py1intro,name='py1intro'),
    path('py2syntax', views.py2syntax,name='py2syntax'),
    path('py3variable', views.py3variable,name='py3variable'),
    path('py4datatype',views.py4datatype,name='py4datatype'),
    path('py5string',views.py5string,name='py5string'),
    path('py6arrays',views.py6arrays,name='py6arrays'),
    path('py7loops',views.py7loops,name='py7loops'),
    path('py8list',views.py8list,name='py8list'),
    path('py9tuple',views.py9tuple,name='py9tuple'),
    path('py10set',views.py10set,name='py10set'),
    path('py11if',views.py11if,name='py11if'),
    path('py12func',views.py12func,name='py12func'),
    path('py13lamda',views.py13lamda,name='py13lamda'),
    path('py14class',views.py14class,name='py14class'),
    path('py15inhe',views.py15inhe,name='py15inhe'),
    path('py16iter',views.py16iter,name='py16iter'),
    path('py17poly',views.py17poly,name='py17poly'),
    # path('javab', views.javab,name='javab'),
    path('j1intro', views.j1intro,name='j1intro'),
    path('j2syntax', views.j2syntax,name='j2syntax'),
    path('j3variable', views.j3variable,name='j3variable'),
    path('j4datatype',views.j4datatype,name='j4datatype'),
    path('j5string',views.j5string,name='j5string'),
    path('j6arrays',views.j6arrays,name='j6arrays'),
    path('j7loops',views.j7loops,name='j7loops'),
    path('j8if',views.j8if,name='j8if'),
]