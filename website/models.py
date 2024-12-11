from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service(models.Model):
    image = models.ImageField(upload_to='website/', blank=True, null=True)
    title = models.CharField(max_length=155)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    customer = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer} - {self.total}"
    


class Appointment(models.Model):
    patient = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient} - {self.date.strftime('%Y-%m-%d %H:%M')}"




class SurveyAnswer(models.Model):
    survey_id = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return f"Survey {self.survey_id}: {self.question[:50]} - {self.answer[:50]}"


 # models.py


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
'''
    # models.py in your website app
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields here
    pass

# website/models.py
from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=100)
    contact_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.username
    

    # website/models.py
from django.db import models

class Booking(models.Model):
    username = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.username} - {self.service}"

'''

    


   
