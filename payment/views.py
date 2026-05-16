

from django.shortcuts import render, redirect
from payment.forms import discharge_summary_form
from payment.models import DischargeSummary
from django.contrib.auth.decorators import login_required
from labreports.models import Lab_test

ROOM_DATA = {
    'COMMON': {'bed': 250, 'nursing': 300, 'doctor': 250, 'misc': 100},
    'SEMI': {'bed': 1000, 'nursing': 1000, 'doctor': 550, 'misc': 250},
    'PRIVATE_AC': {'bed': 1500, 'nursing': 1350, 'doctor': 650, 'misc': 250},
    'PRIVATE_NON_AC': {'bed': 1250, 'nursing': 1150, 'doctor': 650, 'misc': 300},
    'DELUX': {'bed': 2000, 'nursing': 1500, 'doctor': 850, 'misc': 500},
}
MEDICINE_PERCENT = {
    'COMMON': 0.10,
    'SEMI': 0.12,
    'PRIVATE_AC': 0.15,
    'PRIVATE_NON_AC': 0.13,
    'DELUX': 0.20,
}

@login_required(login_url="login")
def discharge(request):
    if request.method == 'POST':
        form = discharge_summary_form(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)

            days = (obj.discharge_date - obj.admission_date).days
            if days <= 0:
                days = 1
            obj.total_days = days

            data = ROOM_DATA[obj.room_type]

            bed = data['bed']
            nursing = data['nursing']
            doctor = data['doctor']
            misc = data['misc']

            obj.room_charges = bed * days
            obj.nursing_charges = nursing * days
            obj.doctor_charges = doctor * days
            misc_total = misc * days

            if obj.food_required:
                obj.food_charges = 480 * days
            else:
                obj.food_charges = 0

            subtotal = (
                obj.room_charges +
                obj.nursing_charges +
                obj.doctor_charges +
                obj.food_charges +
                misc_total
            )

            percent = MEDICINE_PERCENT[obj.room_type]
            obj.medicine_charges = int(subtotal * percent)

            obj.total_bill = subtotal + obj.medicine_charges

            obj.save()

            return redirect('final_bill', id=obj.id)

    else:
        form = discharge_summary_form()

    return render(request, 'payment/discharge.html', {'form': form})


@login_required(login_url="login")
def final_bill(request, id):
    bill = DischargeSummary.objects.get(id=id)
    return render(request, 'payment/final_bill.html', {'bill': bill})

@login_required(login_url="login")
def discharge_list(request):
    bills = DischargeSummary.objects.all().order_by('-id')
    return render(request, 'payment/discharge_list.html', {'bills': bills})

@login_required(login_url="login")
def hospital_charges(request):

    room_data = {
        'COMMON': {'bed': 250, 'nursing': 300, 'doctor': 250, 'misc': 100},
        'SEMI': {'bed': 1000, 'nursing': 1000, 'doctor': 550, 'misc': 250},
        'PRIVATE_AC': {'bed': 1500, 'nursing': 1350, 'doctor': 650, 'misc': 250},
        'PRIVATE_NON_AC': {'bed': 1250, 'nursing': 1150, 'doctor': 650, 'misc': 300},
        'DELUX': {'bed': 2000, 'nursing': 1500, 'doctor': 850, 'misc': 500},
    }

    tests = Lab_test.objects.all()   

    return render(request, 'payment/hospital_charges.html', {
        'room_data': room_data,
        'tests': tests,
        'food_charge': 480
    })
    
