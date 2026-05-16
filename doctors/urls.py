from django.urls import path
from doctors import views

urlpatterns=[
    path("",views.alldoc,name="alldoctors"),
    path("treatments",views.alltreatments,name="treatments"),
    path('book_treatments/', views.book_treatments, name='book_treatments'),
    path('book_doctors/<int:id>/', views.book_doctors, name='book_doctors'),
    path('appointmentform/<int:id>/', views.appointmentform, name='appointmentform'),
]
 