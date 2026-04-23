from django import forms
from skilllinkapp.models import  freelancer

class FreelancerProfileForm(forms.ModelForm):
    class Meta:
        model = freelancer
        fields = ['name', 'email', 'category','skills', 'education', 'mobile']