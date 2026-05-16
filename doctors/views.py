from django.shortcuts import render,redirect
from doctors.models import Alldoctors,Alltreatments
from doctors.forms import AppointmentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def alldoc(request):
    doctors = Alldoctors.objects.all() 
    return render(request,'doctors/alldoctors.html', {"doctors": doctors})

@login_required(login_url="login")
def alltreatments(request):
    treatments = Alltreatments.objects.select_related('doctor_name').all()
    return render(request,'doctors/alltreatments.html', {'treatments': treatments})

@login_required(login_url="login")
def book_treatments(request):
    treatments = Alltreatments.objects.all()
    return render(request, "doctors/book_treatments.html", {
        'treatments': treatments
    })

@login_required(login_url="login")
def book_doctors(request, id):
    treatments = Alltreatments.objects.get(id=id)
    # doctors = Alldoctors.objects.filter(alltreatments=treatments)
    doctors = Alldoctors.objects.filter(specialized__iexact=treatments.Category   )
    return render(request, 'doctors/book_doctors.html', {
        'treatments': treatments,
        'doctors': doctors
    })

from django.contrib import messages

@login_required(login_url="login")
def appointmentform(request, id):
    doctor = Alldoctors.objects.get(id=id)

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)  
            appointment.consultation_charge = 550  
            appointment.user = request.user 
            appointment.save()
            messages.success(request, "Appointment Confirmed Successfully!")

            return redirect('home')


    else:
        form = AppointmentForm(initial={
            'doctorname': doctor.name,
            'category': doctor.specialized,
            'consultation_charge': 550
        })

    return render(request, 'doctors/appointmentform.html', {"form": form})