from django.db import models
from django.contrib.auth.models import AbstractUser
# q: HOW TO CREATE  custom user model   a: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

class User(AbstractUser):
    GENDER=(('MAIL','MAIL'),('FEMAIL','FEMAIL'))

    public_visibility=models.BooleanField(default=False)
    city=models.CharField(max_length=100, blank=True)
    state=models.CharField(max_length=100, blank=True)
    age=models.IntegerField(blank=True, null=True)
    DOB=models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=100, choices=GENDER, blank=True)


    def __str__(self):
        return self.first_name+" "+self.last_name