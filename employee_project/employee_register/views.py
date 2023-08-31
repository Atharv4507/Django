from http.client import HTTPResponse
import mimetypes
import os
from urllib import request
from django.shortcuts import render
from django.shortcuts import redirect
# from employee_register import views
from employee_register.forms import EmployeeForm
from employee_register.models import Employee
from employee_register.models import Position
from employee_register.models import Advertising
# Create your views here.


def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
            return render(request, "employee_form.html", {'form': form})
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
            return render(request, "employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                print("hi")
                form.save()
                return redirect('/success/')
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/success/')


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/success/')


def upload_csv(request):
    return render(request, "upload_csv.html")
'''
data = {}
if "GET" == request.method:
    return render(request, "employee_register/upload_csv.html",data)
    # if not GET, then proceed
try:
    csv_file = request.FILES["csv_file"]
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File is not CSV type')
        return HttpResponseRedirect(reverse("employee_register:upload_csv"))
    # if file is too large, return
    if csv_file.multiple_chunks():
        messages.error(request, "Uploaded file is too big (%.2f MB)." %
                       (csv_file.size/(1000*1000),))
        return HttpResponseRedirect(reverse("employee_register:upload_csv"))

    file_data = csv_file.read().decode("utf-8")

    lines = file_data.split("\n")
    # loop over the lines and save them in db. If error , store as string and then display
    for line in lines:
        fields = line.split(",")
        data_dict = {}
        data_dict["TV"] = fields[0]
        data_dict["Radio"] = fields[1]
        data_dict["Newspaper"] = fields[2]
        data_dict["Sales"] = fields[3]
        try:
            form = EventsForm(data_dict)
            advertising = Advertising.objects.get()
            form = Advertising(request.POST, instance=advertising)
            if form.is_valid():
                form.save()
            else:
                logging.getLogger("error_logger").error(form.errors.as_json())
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            pass

    except Exception as e:
        logging.getLogger("error_logger").error(
            "Unable to upload file. "+repr(e))
        messages.error(request, "Unable to upload file. "+repr(e))

return HttpResponseRedirect(reverse("employee_register:upload_csv"))
'''

def upload_file(request):
    fm2 = upload_file(request.POST)
    return render(request, "upload_file.html", {'form': fm2})


def upload_file(request):
    return render(request, "upload_file.html")


def download_csv_file(request, filename=''):
    if filename != '':
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/downloadapp/Files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HTTPResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        return render(request, 'file.html')
