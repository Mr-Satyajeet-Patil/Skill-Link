from urllib import request
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import company
from .models import freelancer
from django.contrib.auth.hashers import make_password

def base(request):
    return render(request, 'base.html')


def joinnow(request):
    return render(request, 'joinnow.html')