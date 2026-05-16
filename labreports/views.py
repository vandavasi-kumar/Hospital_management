from django.shortcuts import render, redirect
from labreports.forms import LabTechRegisterationForm,LabTestForm
from labreports.models import Lab_report,Lab_test,Lab_test
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



def labTechReg(request):

    if request.method == 'POST':
        form = LabTechRegisterationForm(request.POST)

        if form.is_valid():
            user = form.save()

            Lab_report.objects.create(
                user=user,
                emp_id=form.cleaned_data['emp_id'],
                qualification=form.cleaned_data['qualification'],
                yop=form.cleaned_data['yop'],
                address=form.cleaned_data['address']
            )

        
            return redirect('dashboard')  # or same page

    else:
        form = LabTechRegisterationForm()

    return render(request, 'labreports/labTechReg.html', {'form': form})

@login_required(login_url="login")
def all_tests(request):
    tests = Lab_test.objects.all()
    return render(request, 'labreports/all_tests.html', {'tests': tests})

@login_required(login_url="login")
def dashboard(request):
    tests = Lab_test.objects.all()
    paginator=Paginator(tests,5)     
    page_number=request.GET.get('page')
    tests=paginator.get_page(page_number)
    labtech = getattr(request.user, 'lab_report', None)
    return render(request, 'labreports/dashboard.html', {'tests': tests,'labtech':labtech})



@login_required(login_url="login")
def add_lab_test(request):

    if request.method == 'POST':
        form = LabTestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = LabTestForm()

    return render(request, 'labreports/add_lab_test.html', {'form': form})

@login_required(login_url="login")
def edit_lab_test(request, id):
    test = Lab_test.objects.get(id=id)

    if request.method == "POST":
        form = LabTestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = LabTestForm(instance=test)

    return render(request, 'labreports/edit_lab_test.html', {'form': form})