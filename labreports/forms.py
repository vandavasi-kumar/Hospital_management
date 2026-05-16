from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from labreports.models import Lab_test



class LabTechRegisterationForm(UserCreationForm):
    emp_id=forms.CharField( max_length= 10, required=False)
    qualification=forms.CharField(max_length=20,required=True)
    address=forms.CharField(max_length=100,required=True)
    yop=forms.IntegerField()
    class Meta:
        model=User
        fields=['username','email']  
        

class LabTestForm(forms.ModelForm):
    class Meta:
        model = Lab_test
        # fields = ['reffered_by','patient_name','lab_test','lab_results']
        fields='__all__'