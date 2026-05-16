from django import forms
from payment.models import DischargeSummary

class discharge_summary_form(forms.ModelForm):
    class Meta:
        model = DischargeSummary
        fields = '__all__'
        exclude = [
            'total_days', 
            'room_charges',
            'doctor_charges',
            'nursing_charges',
            'medicine_charges',
            'food_charges',
            'total_bill',
        ]

        widgets = {
            'admission_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'discharge_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['patient_name'].empty_label = "Select Patient"
        self.fields['doctor'].empty_label = "Select Doctor"