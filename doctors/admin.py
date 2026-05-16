from django.contrib import admin

# Register your models here.
from doctors.models import Alldoctors,Alltreatments,Appointment
admin.site.register(Alldoctors)
admin.site.register(Alltreatments)
admin.site.register(Appointment)
