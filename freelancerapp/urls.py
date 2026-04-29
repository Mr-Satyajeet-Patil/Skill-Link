
from django.urls import include, path

from freelancerapp import views
app_name = 'freelancerapp'

urlpatterns = [
    
    path('freelancerlogin/', views.freelancerlogin, name='freelancerlogin'),
    path('freelancersignup/', views.freelancersignup, name='freelancersignup'),
    path('freelancerpanel/', views.freelancerpanel, name='freelancerpanel'),
    path('managefreelancer/', views.manage_profile, name= 'managefreelancer'),
    path('findproject/', views.find_project, name='findproject'),
    path('placebid/<int:project_id>/', views.place_bid, name='placebid'),
    path('freelancerlogout/', views.freelancerlogout, name='freelancerlogout'),
    path('mybids/', views.mybids, name='mybids'),
]