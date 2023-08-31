from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import ProgressReport,Services
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# def sign(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         fname = request.POST.get('first_name')
#         lname = request.POST.get('last_name')
#         # mobile = request.POST.get('mobile') 
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
        
#         if pass1!=pass2:
#             messages.warning(request,"you'r passwords dosen't matching")
#             # return HttpResponse("request,you'r passwords dosen't matching")
#         else:
#             # my_user = User.objects.create_user(email,fname,lname,mobile,pass1)
#             my_user = User(email=email,first_name=fname,last_name=lname,password=pass1)
#             my_user.save()
#             return redirect('loginp')
#         print(fname,lanme,email,pass1,pass2)
#     return render(request, 'sign.html')

# def loginp(request):
#     if request.method=="POST":
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password')
#         user = authenticate(request, email=email, password=pass1)
#         # user = User(email=email,password=pass1)
#         print(email,pass1)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#             # messages.warning(request, "Username or password is incorrect")
#         else:
#             # login(request, user)
#             # return redirect('home')
#             messages.warning(request, "Username or password is incorrect")
        
#     return render(request, 'loginp.html')

def sign(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1!=pass2:
            messages.warning(request,"you'r passwords dosen't matching")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('loginp')
        print(uname,email,pass1,pass2)
    return render(request, 'sign.html')

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
        
    return render(request, 'loginp.html')

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
        name = request.POST.get("name")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        services = Services(name=name,email=email,phone=phone,desc=desc,date = datetime.today())
        services.save()
        messages.success(request, 'Your Profile details updated.')
    return render(request, 'services.html')
    # return HttpResponse("This is services page")


@login_required
def profile(request):
    user = request.user
    progress_reports = ProgressReport.objects.filter(user=user)
    return render(request,'profile.html')

def pl(request):
    return render(request, 'programming/pl.html')

def lang(request):
    return render(request, 'language/lang.html')

def pythonb(request):
    return render(request, 'pythonb.html')

def py1intro(request):
    return render(request, 'programming/py1intro.html')

def py2syntax(request):
    return render(request, 'programming/py2syntax.html')

def py3variable(request):
    return render(request, 'programming/py3variable.html')

def py4datatype(request):
    return render(request, 'programming/py4datatype.html')

def py5string(request):
    return render(request, 'programming/py5string.html')

def py6arrays(request):
    return render(request, 'programming/py6arrays.html')

def py7loops(request):
    return render(request, 'programming/py7loops.html')

def py8list(request):
    return render(request, 'programming/py8list.html')

def py9tuple(request):
    return render(request, 'programming/py9tuple.html')

def py10set(request):
    return render(request, 'programming/py10set.html')

def py11if(request):
    return render(request, 'programming/py11if.html')

def py12func(request):
    return render(request, 'programming/py12func.html')

def py13lamda(request):
    return render(request, 'programming/py13lamda.html')

def py14class(request):
    return render(request, 'programming/py14class.html')

def py15inhe(request):
    return render(request, 'programming/py15inhe.html')
    
def py16iter(request):
    return render(request, 'programming/py16iter.html')
    
def py17poly(request):
    return render(request, 'programming/py17poly.html')


def j1intro(request):
    return render(request, 'java/j1intro.html')

def j2syntax(request):
    return render(request, 'java/j2syntax.html')

def j3variable(request):
    return render(request, 'java/j3variable.html')

def j4datatype(request):
    return render(request, 'java/j4datatype.html')

def j5string(request):
    return render(request, 'java/j5string.html')

def j6arrays(request):
    return render(request, 'java/j6arrays.html')

def j7loops(request):
    return render(request, 'java/j7loops.html')

def j8if(request):
    return render(request, 'java/j8if.html')