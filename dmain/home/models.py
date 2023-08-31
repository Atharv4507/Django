from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# User= settings.AUTH_USER_MODEL
# Create your models here
class u(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth import authenticate,login,logout
from datetime import datetime
# Create your models here.

# class CustomUserManger(BaseUserManager):
#     def _create_user(self,email,password,first_name,last_name,mobile, **extra_fileds):
#         if not email:
#             raise ValueError("Email must be provided")
#         if not password:
#             raise ValueError("Password must be provided")
        
#         user = self.model(
#             email = self.normalize_email(email),
#             first_name = first_name,
#             last_name = last_name,
#             mobile = mobile,
#             **extra_fileds
#         )
#         user.set_password(password)
#         user.save()
#         return user

#         # def authenticate(self,email,password):     
        
#     def create_user(self,email,password,first_name,last_name,mobile, **extra_fileds):
#         extra_fileds.setdefault('is_staff',True)
#         extra_fileds.setdefault('is_active',True)
#         extra_fileds.setdefault('is_superuser',True)
#         return self._create_user(email,password,first_name,last_name,mobile,password,**extra_fileds)
    
#     def create_superuser(self,email,password,first_name,last_name,mobile, **extra_fileds):
#         extra_fileds.setdefault('is_staff',True)
#         extra_fileds.setdefault('is_active',True)
#         extra_fileds.setdefault('is_superuser',True)
#         return self._create_user(email,password,first_name,last_name,mobile, **extra_fileds)  
        
#     # def authenticate(email,password): 
#     #     extra_fileds.setdefault('is_staff',True)
#     #     extra_fileds.setdefault('is_active',True)
#     #     if  (email==email and password==password):
    
            
    

# class User(AbstractBaseUser,PermissionsMixin):
    
#     email = models.EmailField(db_index=True,unique=True,max_length=130)
#     first_name = models.CharField(max_length=140)
#     last_name = models.CharField(max_length=140)
#     mobile = models.CharField(max_length=140)
#     address = models.CharField(max_length=140)
#     # date = models.DateField(auto_created=True)
    
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=True)
    
#     objects = CustomUserManger()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name', 'mobile']
    
#     class Meta:
#         verbose_name = "User"
#         verbose_name_plural = "Users"
        

class Services(models.Model):
    # Board, on_delete=models.CASCADE, related_name='topics'
    # user= models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=True)
    name  = models.CharField(max_length=130)
    email = models.CharField(max_length=130)
    phone = models.CharField(max_length=130)
    desc = models.TextField()
    date = models.DateField()
      
    def __str__(self):
        return self.name
