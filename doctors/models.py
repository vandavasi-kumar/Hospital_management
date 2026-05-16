from django.db import models
from django.contrib.auth.models import User


# Create your models here.

specialization=[
    ('GENERAL MEDICIENE','General Medicine'),
    ('CARDIOLOGIST','cardiologist'),
    ('ORTHOPEDIC','orthopedic'),
    ('EYE SPECIALIST','eye specialist'),
    ('ENT','ent'),
    ('DENTIST','dentist'),
    ('NUEROLOGIST','nuerologist'),
    ('GYNOCOLOGIST','Gynocologist'),
    ('CHILD SPECIALIST','Child Specialist'),
    
    ('OTHERS','other'),
    
]

class Alldoctors(models.Model):
    name=models.CharField(max_length=100)
    specialized=models.CharField(choices=specialization)
    YOE=models.PositiveIntegerField()
    lic_no=models.CharField(max_length=50)
    certification=models.ImageField(upload_to='certificates/',blank=True,null=True)
    profile_pic = models.ImageField(upload_to='doctors/', blank=True, null=True)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100)
    phone=models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name


class Alltreatments(models.Model):
    treatmentname = models.CharField(max_length=100)
    Category = models.CharField(choices=specialization)
    doctor_name = models.ForeignKey(Alldoctors, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)


    def __str__(self):
        return self.treatmentname
    
    
    
class Appointment(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctorname = models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    consultation_charge = models.CharField(max_length=5,default=550)

    def __str__(self):
        return self.doctorname
    
    