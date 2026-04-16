from django import forms
from skilllinkapp.models import company

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['companyname', 'email', 'industrytype', 'contact', 'location']