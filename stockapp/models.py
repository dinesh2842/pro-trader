from django.db import models
from django.contrib.auth.models import User
#from datetime import datetime, date
#from ckeditor.fields import RichTextField
#from django.db.models.base import Model
#from django.db.models.signals import pre_save
#from blog.utils import unique_slug_generator
from django.contrib.auth.models import AbstractUser
#from django.contrib.admin.models import LogEntry
#from stockapp.models import CustomUser

class contact_us(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField()
    # phone= models.CharField(max_length=12)
    subject= models.CharField(max_length=50)
    number= models.CharField(max_length=20)
    message = models.TextField(default='hello')
    #date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username