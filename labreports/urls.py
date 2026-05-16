from django.urls import path
from labreports import views

urlpatterns=[
    path("labTechReg",views.labTechReg,name="labTechReg"),
    path('all_tests/', views.all_tests, name='all_tests'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_lab_test/', views.add_lab_test, name='add_lab_test'),
    path('edit-lab-test/<int:id>/', views.edit_lab_test, name='edit_lab_test'),

]
