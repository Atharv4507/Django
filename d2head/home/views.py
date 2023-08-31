import http
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from home.functions import handle_uploaded_file
from home.forms import StudentForm

def index(request):
    if request.method=='POST':
        student = StudentForm(request.POST,request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfuly")
    else:
        student = StudentForm()
        return render(request,"index.html",{'form':student})
    # return HttpResponse("Hello")

def home1(request):
    return render(request,"home1.html")