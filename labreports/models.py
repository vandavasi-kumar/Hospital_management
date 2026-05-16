from django.db import models

from django.db import models
from learnapp.models import UserDetails
from django.contrib.auth.models import User
from doctors.models import Alldoctors


# Create your models here.
class Lab_report(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    yop=models.IntegerField()
    address=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.username} ({self.emp_id})"

class Lab_test(models.Model):
    All_lab_tests = [
        ("BLOOD TEST", "Blood Test"),
        ("URINE TEST", "Urine Test"),
        ("X-RAY", "X-Ray"),
        ("MRI", "MRI"),
        ("CT SCAN", "CT Scan"),
        ("ULTRASOUND", "Ultrasound"),
        ("ECG", "ECG"),
        ("EEG", "EEG"),
        ("BIOPSY", "Biopsy"),
        ("ALLERGY TEST", "Allergy Test"),
    ]
    test_result=[
        ('pending','Pending'),
        ('ongoing','Ongoing'),
        ('completed','Completed')
    ]


    test_range = [
        ('nil','Nil'),
        ('positive','Positive'),
        ('negative','Negative'),
        ('normal','Normal'),
        ('abnormal','Abnormal')
    ]
    reffered_by = models.ForeignKey(Alldoctors,on_delete=models.CASCADE)
    patient_name = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    lab_test = models.CharField(max_length=100, choices=All_lab_tests)
    lab_results = models.CharField(max_length=500, choices=test_result,default='ongoing')
    created_at = models.DateTimeField(auto_now_add=True)
    result_range = models.CharField(max_length=100, choices=test_range,default='Nil')
    result_description = models.TextField(max_length=500)
    test_cost = models.IntegerField(default=500)
    test_duration = models.CharField(max_length=50, default="4 hrs")

    def __str__(self):
        return f"{self.lab_test} - {self.patient_name}"