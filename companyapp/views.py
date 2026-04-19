from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from skilllinkapp.models import company

from django.shortcuts import render, redirect
from skilllinkapp.models import project

from .forms import CompanyProfileForm


def companypanel(request):
    company_id = request.session.get('company_id')

    if not company_id:
        return redirect('companylogin')

    comp = company.objects.get(id=company_id)

    return render(request, 'company/companypanel.html', {'company': comp})
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

    return render(request, 'company/companysignup.html')



def companyloginview(request):
    next_url = request.GET.get('next') or request.POST.get('next')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        comp = company.objects.filter(email=email).first()

        if comp and comp.password == password:
            request.session['company_id'] = comp.id
            request.session['company_name'] = comp.companyname

            if next_url:
                return redirect(next_url)

            return redirect('companyapp:companypanel')

        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'company/companylogin.html')

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

    return render(request, 'company/managecompany.html', {'form': form})




def postproject(request):

    print("SESSION:", request.session.get('company_id'))

    company_id = request.session.get('company_id')

    # 🔴 Not logged in → redirect to login
    if not company_id:
        return redirect('/company/login/?next=/company/postproject/')

    # 🔴 Safe fetch
    try:
        company_obj = company.objects.get(id=int(company_id))
    except (ValueError, company.DoesNotExist):
        return redirect('/company/login/?next=/company/postproject/')

    # 🔴 Handle form
    if request.method == 'POST':
        action = request.POST.get('action')
        pid = request.POST.get('id')

        data = {
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'requiredskills': request.POST.get('requiredskills'),
            'budget': request.POST.get('budget'),
            'duration': request.POST.get('duration'),
        }

        if action == 'add':
            project.objects.create(companyname=company_obj, **data)

        elif action == 'update' and pid:
            project.objects.filter(id=pid, companyname=company_obj).update(**data)

        elif action == 'delete' and pid:
            project.objects.filter(id=pid, companyname=company_obj).delete()

        return redirect('companyapp:postproject')

    # 🔴 Fetch projects
    projects = project.objects.filter(companyname=company_obj)

    return render(request, 'company/postproject.html', {'projects': projects})