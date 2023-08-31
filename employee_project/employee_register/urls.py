from django.contrib import admin
from django.urls import path,include
from employee_register import views
urlpatterns = [
    path('',views.employee_form,name="employee_insert"),
    path('upload_csv/',views.upload_csv,name="upload_csv"),
    path('upload_file/',views.upload_file,name="upload_file"),
    path('employee_list/',views.employee_list),
    path('success/',views.employee_list,name="employee_list"),
    path('delete/<int:id>/',views.employee_delete,name="employee_delete"),
    path('<int:id>/',views.employee_form,name="employee_update"),
    # path('download/', views.download_file),
    # path('downloadcsv/', views.download_csv_file, name='download_csv_file')
]