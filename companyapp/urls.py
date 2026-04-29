
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
        path('biddetails/', views.bid_details, name='biddetails'),
        path('freelancerprofile/<int:freelancer_id>/', views.freelancer_profile, name='freelancerprofile'),
        path('selectfreelancer/<int:bid_id>/', views.select_freelancer, name='selectfreelancer'),
        path('unselectfreelancer/<int:bid_id>/', views.unselect_freelancer, name='unselectfreelancer'),
        path('projectstatus/', views.project_status, name='projectstatus'),
     
]



# companyapp/urls.py



