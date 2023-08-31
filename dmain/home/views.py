from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Services
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.


# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse

def sign(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1!=pass2:
            messages.warning(request,"you'r passwords dosen't matching")
            # return HttpResponse("request,you'r passwords dosen't matching")
        else:
            my_user = User.objects.create_user(uname,fname,lname,email,pass1)
            # my_user = User(username=uname,first_name=fname,last_name=lname,email=email,password=pass1)
            my_user.save()
            return redirect('loginp')
        print(uname,fname,lanme,email,pass1,pass2)
    return render(request, 'logine/sign.html')
    # registration_url = reverse("django_registration_register")
    # test_username = "testuser"
    # post_data = {
    #     "first_name": "TestFirstName",
    #     "last_name": "TestLastName",
    #     "username": test_username,
    #     "email": "testuser@example.com",
    #     "password1": "mypass",
    #     "password2": "mypass"
    # }

    # def test_register(self):
    #     response = self.client.post(self.registration_url, self.post_data)
    #     self.assertRedirects(response, reverse("django_registration_complete"))
    #     user = get_user_model().objects.get(username=self.test_username)
    #     # Assert all fields are present on the newly registered user
    #     for field in ["username", "first_name", "last_name", "email"]:
    #         self.assertEqual(self.post_data[field], getattr(user, field))

def loginp(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(username=username, password=pass1)
        print(username,pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Username or password is incorrect")
        
    return render(request, 'logine/loginp.html')

def contact(request):
    logout(request)
    return redirect("loginp")

def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        services = Services(name=name,email=email,phone=phone,desc=desc,date = datetime.today())
        services.save()
        messages.success(request, 'Your Profile details updated.')
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

# def contact(request):
#     return render(request, 'contact.html')
def pl(request):
    return render(request, 'programming/pl.html')

def lang(request):
    return render(request, 'language/lang.html')

def pythonb(request):
    return render(request, 'pythonb.html')

def py1intro(request):
    return render(request, 'programming/py1intro.html')