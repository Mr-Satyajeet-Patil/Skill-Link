from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from skilllinkapp.models import freelancer
from skilllinkapp.models import freelancer

# Create your views here.

def freelancerlogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            frlns = freelancer.objects.get(email=email, password=password)

            # ✅ login success → create session
            request.session['freelancer_id'] = frlns.id
            request.session['freelancer_name'] = frlns.name

            return redirect('freelancerapp:freelancerpanel')

        except freelancer.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return render(request, 'freelancerapp/freelancerlogin.html')

    return render(request, 'freelancerapp/freelancerlogin.html')

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
            return redirect('freelancerapp:freelancersignup')

        # Check if freelancer already exists
        if freelancer.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('freelancerapp:freelancersignup')

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

     return render(request, 'freelancerapp/freelancersignup.html')
 
