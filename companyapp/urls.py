
from django.urls import include, path

from . import views

def companyloginview(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            comp = company.objects.get(email=email, password=password)

            request.session['company_id'] = comp.id  # ✅ REQUIRED

            return redirect('companypanel')

        except:
            return render(request, 'company/companylogin.html', {'error': 'Invalid credentials'})

    return render(request, 'company/companylogin.html')
app_name = 'companyapp'

urlpatterns = [
        path('companysignup/', views.companysignup, name='companysignup'),
        path('companylogin/', views.companyloginview, name='companylogin'),
        path('companypanel/', views.companypanel, name='companypanel'),
        path('managecompany/', views.manage_profile, name= 'managecompany'),
        path('postproject/', views.postproject, name='postproject'),
]



# companyapp/urls.py



