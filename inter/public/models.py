from django.db import models

# Create your models here.

class manage(models.Model):
    title=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=50,null=True)
    img=models.ImageField(upload_to='img',null=True)



from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser




class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    user_type = models.CharField(max_length=20)
    # Add any other fields you need

