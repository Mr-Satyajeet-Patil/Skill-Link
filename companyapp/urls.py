
from django.urls import include, path

from . import views


app_name = 'companyapp'

urlpatterns = [
        path('companysignup/', views.companysignup, name='companysignup'),
        path('companylogin/', views.companyloginview, name='companylogin'),
        path('companypanel/', views.companypanel, name='companypanel'),
        path('managecompany/', views.manage_profile, name= 'managecompany'),
        path('postproject/', views.postproject, name='postproject'),
        path('companylogout/', views.companylogout, name='companylogout'),
        path('listofprojects/', views.listofprojects, name='listofprojects'),
]



# companyapp/urls.py



