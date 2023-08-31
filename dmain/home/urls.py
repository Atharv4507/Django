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
    path('pl', views.pl, name='pl'),
    path('lang', views.lang,name='lang'),
    # path('pythonb', views.pythonb,name='pythonb'),
    path('py1intro', views.py1intro,name='py1intro'),
    # path('logine/sign/',RegistrationView.as_view(form_class=RegistrationWithNameForm),name='django_registration_register',),
    # path("logine/", include("django_registration.backends.activation.urls")),
]