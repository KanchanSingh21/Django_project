from django.db import models

# Create your models here.

class signup_details(models.Model):
    username=models.CharField(max_length=50)
    mydate=models.CharField(max_length=50)
    myemail=models.CharField(max_length=50)
    fullAddress=models.CharField(max_length=50)
    myGender=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

