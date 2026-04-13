from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import company
from .models import freelancer
from django.contrib.auth.hashers import make_password

def base(request):
    return render(request, 'base.html')



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
            return redirect('companysignup')

        # Check if company already exists
        if company.objects.filter(companyname=companyname).exists():
            messages.error(request, "Username already exists")
            return redirect('companysignup')

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

    return render(request, 'companysignup.html')

from django.shortcuts import render, redirect
from .models import company

def companyloginview(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            comp = company.objects.get(email=email, password=password)

            # ✅ login success → create session
            request.session['company_id'] = comp.id
            request.session['company_name'] = comp.companyname

            return redirect('companydashboard')

        except company.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return render(request, 'companylogin.html')

    return render(request, 'companylogin.html')
# Create your views here.


def companydashboard(request):
    return render(request, 'companydashboard.html')
    
def freelancerlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            frlns = freelancer.objects.get(email=email, password=password)

            # ✅ login success → create session
            request.session['freelancer_id'] = frlns.id
            request.session['freelancer_name'] = frlns.name

            return redirect('freelancerdashboard')

        except freelancer.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return render(request, 'freelancerlogin.html')

    return render(request, 'freelancerlogin.html')

def freelancersignup(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        contact = request.POST.get('mobile')
        category = request.POST.get('category')
        skills = request.POST.get('skills')

        education = request.POST.get('education')

        # Password match check
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('freelancersignup')

        # Check if freelancer already exists
        if freelancer.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('freelancersignup')

        # Save data (with hashed password)
        new_freelancer = freelancer(
            name=name,
            email=email,
            password=(password1), # In production, use make_password(password1) to hash the password
            skills=skills,
            contact=contact,
            education=education,
            category=category
        )
        new_freelancer.save()

        messages.success(request, "Account created successfully")
        #return redirect('companylogin')

     return render(request, 'freelancersignup.html')
 
 
def joinnow(request):
    return render(request, 'joinnow.html')