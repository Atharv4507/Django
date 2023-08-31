# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Services
from django.contrib import messages

#for  logine and sign up page
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def sign(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1!=pass2:
            messages.warning(request,"you'r passwords dosen't matching")
            # return HttpResponse("request,you'r passwords dosen't matching")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginp')
        print(uname,email,pass1,pass2)
    return render(request, 'logine/sign.html')

def loginp(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(username=username, password=pass1)
        print(username,pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
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

def courses(request):
    return render(request, 'courses.html')

def kaushik(request):
    return render(request, 'doctor/kaushik.html')