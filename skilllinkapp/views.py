from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import enquiry as Enquiry


from urllib import request
from django.contrib.auth import authenticate, login

from django.shortcuts import render,redirect
from .models import company
from .models import freelancer
from django.contrib.auth.hashers import make_password

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



 

def enquiry(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

       
        Enquiry.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            message=message,
        )

       
        messages.success(request, "Enquiry submitted successfully!")
       
        return redirect('enquiry')

    return render(request, 'enquiry.html')


def joinnow(request):
    return render(request, 'joinnow.html')
