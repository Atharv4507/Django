from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout
from datetime import datetime
# Create your models here.
 

class Services(models.Model):
    # Board, on_delete=models.CASCADE, related_name='topics'
    # user= models.ForeignKey(User,on_delete=models.CASCADE,default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name  = models.CharField(max_length=130)
    email = models.CharField(max_length=130)
    phone = models.CharField(max_length=130)
    # desc = models.CharField( max_length=130)
    desc = models.TextField()
    date = models.DateField()
      
    def __str__(self):
        return self.name
    




# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None,first_name=None,last_name=None,mobile=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email, 
#             first_name = first_name,
#             last_name = last_name,
#             mobile = mobile, 
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None,first_name=None,last_name=None,mobile=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password,first_name,last_name,mobile, **extra_fields)

# class HomeUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     mobile = models.CharField(max_length=140)
#     address = models.CharField(max_length=140)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name','mobile']

#     objects = UserManager()

#     def __str__(self):
#         return self.email

class ProgressReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    progress = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s Progress Report"