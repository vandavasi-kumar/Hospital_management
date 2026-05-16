from django.shortcuts import render,redirect
from learnapp.forms import UserForm,Userprofile,UserUpdateForm,UserProfileUpdateForm
from django.contrib.auth import authenticate,login,logout

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from doctors.models import Appointment
from labreports.models import Lab_report

# Create your views here.

def registeration(request):
    registered=False
    if request.method=='POST':
        
        form1=UserForm(request.POST)
        form2=Userprofile(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            
            profile=form2.save(commit=False)
            profile.user=user #merging the form 2 and form 1 data
            profile.save()
            registered=True
        
            
    else:
        form1=UserForm()
        form2=Userprofile()
        
    context={
        'form1':form1,
        'form2':form2,
        'registered':registered
    }
    return render(request,"registeration.html",context)

def user_login(request):
    if request.method=="POST":
        username=request.POST['username']   
        password=request.POST['password'] 
        # print(username)  
        # print(password)
        user=authenticate(username=username,password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return redirect("home")
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("please check the creds....!!!")
        
    return render(request,'login.html',{})

@login_required(login_url="login")

def home(request):

    labtech = None

    if request.user.is_authenticated:
        try:
            labtech = Lab_report.objects.get(user=request.user)
        except Lab_report.DoesNotExist:
            labtech = None

    return render(request, 'home.html', {
        'labtech': labtech
    })

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")

# @login_required(login_url="login")
# def user_profile(request):
#     return render(request,'profile.html',{})
@login_required(login_url="login")
def user_profile(request):
    appointments = Appointment.objects.filter(user=request.user)  

    return render(request, 'profile.html', {
        'appointments': appointments
    })

@login_required(login_url="login")
def user_update(request):
    if request.method=='POST':
        form1=UserUpdateForm(request.POST,instance=request.user)
        form2=UserProfileUpdateForm(request.POST,request.FILES,instance=request.user.userdetails)

        
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            profile=form2.save(commit=False)
            profile.user=user 
            profile.save()
            
            return redirect('profile')
    else:
        form1=UserUpdateForm(instance=request.user)
        form2=UserProfileUpdateForm(instance=request.user.userdetails)
    return render(request,'update.html',{'form1':form1,'form2':form2})



