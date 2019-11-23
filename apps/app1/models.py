from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        
        existingEmail=User.objects.filter(email=postData['email'])

        if not postData['email']:
            errors['email']= "Email is required"
        elif '@' not in postData['email'] or '.' not in postData['email']:
            errors['email']= "Email must be valid"
        elif existingEmail:
            errors['email']="Email is already assigned to a current User"
        
        if not postData['password']: 
            errors['password']= "Password is required"
        elif postData['password'] != postData['confirm_password']:
            errors['password']= "Password and Confirm password fields are different"
        
        return errors

class User(models.Model):
    email=models.TextField(max_length=30)
    password=models.TextField(max_length=50)
    balance=models.IntegerField(default=0)
    status=models.BooleanField(default=0)
    lat=models.DecimalField(default=0.00, max_digits=10, decimal_places=7)
    lng=models.DecimalField(default=0.00, max_digits=10, decimal_places=7)
    objects=UserManager()
class Driver(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    status=models.IntegerField(default=0)
    lat=models.DecimalField(default=0.00, max_digits=10, decimal_places=7)
    lng=models.DecimalField(default=0.00, max_digits=10, decimal_places=7)