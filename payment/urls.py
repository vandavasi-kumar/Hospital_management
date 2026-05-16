from django.urls import path
from payment import views

urlpatterns = [
    path('discharge/', views.discharge, name='discharge'),
    path('final_bill/<int:id>/', views.final_bill, name='final_bill'),
    path('discharge_list/', views.discharge_list, name='discharge_list'),
    path('hospital-charges/', views.hospital_charges, name='hospital_charges'),
]