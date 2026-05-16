from django.urls import path
from learnapp import views

urlpatterns=[
    path("home",views.registeration,name="register"),
    path("login",views.user_login,name='login'),
    path("",views.home,name='home'),
    path("logout/",views.user_logout,name='logout'),
    path("profile",views.user_profile,name='profile'),
    path("update",views.user_update,name='update'),
    
]
 