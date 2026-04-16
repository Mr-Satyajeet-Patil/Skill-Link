from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from skilllinkapp.models import company



def companypanel(request):
    company_id = request.session.get('company_id')

    if not company_id:
        return redirect('companylogin')

    comp = company.objects.get(id=company_id)

    return render(request, 'companyapp/companypanel.html', {'company': comp})
# Create your views here.


def companysignup(request):
    if request.method == 'POST':
        companyname = request.POST.get('companyname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        industrytype = request.POST.get('industrytype')
        contact = request.POST.get('contact')
        location = request.POST.get('location')

        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('companyapp:companysignup')

        # Check if company already exists
        if company.objects.filter(companyname=companyname).exists():
            messages.error(request, "Username already exists")
            return redirect('companyapp:companysignup')

        # Save data (with hashed password)
        new_company = company(
            companyname=companyname,
            email=email,
            password=(password1), # In production, use make_password(password1) to hash the password
            industrytype=industrytype,
            contact=contact,
            location=location
        )
        new_company.save()

        messages.success(request, "Account created successfully")
        #return redirect('companylogin')

    return render(request, 'companyapp/companysignup.html')



def companyloginview(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            comp = company.objects.get(email=email, password=password)

            # login success → create session
            request.session['company_id'] = comp.id
            request.session['company_name'] = comp.companyname
        
            return redirect('companyapp:companypanel')

        except company.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return render(request, 'companyapp/companylogin.html')

    return render(request, 'companyapp/companylogin.html')

from .forms import CompanyProfileForm

def manage_profile(request):
    company_id = request.session.get('company_id')

    if not company_id:
        return redirect('companyapp:companylogin')

    comp= company.objects.get(id=company_id)

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, instance=comp)
        if form.is_valid():
            form.save()
            return redirect('companyapp:companypanel')
    else:
        form = CompanyProfileForm(instance=comp)

    return render(request, 'companyapp/managecompany.html', {'form': form})