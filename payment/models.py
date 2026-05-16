from django.db import models
from doctors.models import Alldoctors
from django.contrib.auth.models import User


ROOM_CHOICES = [
    ('', 'Select Room Type'),
    ('COMMON', 'Common Ward'),
    ('SEMI', 'Semi Private'),
    ('PRIVATE_AC', 'Private AC'),
    ('PRIVATE_NON_AC', 'Private Non AC'),
    ('DELUX', 'Delux'),
]

class DischargeSummary(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Alldoctors, on_delete=models.CASCADE)

    treatment = models.CharField(max_length=100)
    description = models.TextField()

    admission_date = models.DateField()
    discharge_date = models.DateField()

    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES)
    food_required = models.BooleanField(default=False)

    total_days = models.IntegerField()

    # billing fields
    room_charges = models.IntegerField(default=0)
    doctor_charges = models.IntegerField(default=0)
    nursing_charges = models.IntegerField(default=0)
    medicine_charges = models.IntegerField(default=0)
    food_charges = models.IntegerField(default=0)
    total_bill = models.IntegerField(default=0)

    def __str__(self):
        return self.patient_name