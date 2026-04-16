
from django.urls import include, path

from freelancerapp import views
app_name = 'freelancerapp'

urlpatterns = [
    
    path('freelancerlogin/', views.freelancerlogin, name='freelancerlogin'),
    path('freelancersignup/', views.freelancersignup, name='freelancersignup'),
]