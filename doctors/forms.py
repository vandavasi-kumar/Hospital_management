from django import forms
from doctors.models import Appointment
TIME_SLOTS = [
    ('07:30', '07:30 AM'),
    ('08:00', '08:00 AM'),
    ('08:30', '08:30 AM'),
    ('09:00', '09:00 AM'),
    ('09:30', '09:30 AM'),
    ('10:00', '10:00 AM'),
    ('10:30', '10:30 AM'),
    ('11:00', '11:00 AM'),
    ('11:30', '11:30 AM'),
    ('12:00', '12:00 PM'),
    ('12:30', '12:30 PM'),
    ('13:00', '01:00 PM'),
    ('13:30', '01:30 PM'),
    ('14:00', '02:00 PM'),
    ('14:30', '02:30 PM'),
    ('15:00', '03:00 PM'),
    ('15:30', '03:30 PM'),
    ('16:00', '04:00 PM'),
    ('16:30', '04:30 PM'),
    ('17:00', '05:00 PM'),
    ('17:30', '05:30 PM'),
    ('18:00', '06:00 PM'),
    ('18:30', '06:30 PM'),
    ('19:00', '07:00 PM'),
    ('19:30', '07:30 PM'),
    ('20:00', '08:00 PM'),
    ('20:30', '08:30 PM'),
    ('21:00', '09:00 PM'),
]

class AppointmentForm(forms.ModelForm):
    consultation_charge=forms.CharField(disabled=True, required=False)
    time = forms.ChoiceField(choices=TIME_SLOTS)
    class Meta:
        model = Appointment
        fields = ['doctorname', 'category','date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','min': __import__('datetime').date.today().isoformat()}), 
            'time': forms.TimeInput(attrs={'type': 'time'})  
        }
        