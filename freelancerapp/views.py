from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from freelancerapp.forms import FreelancerProfileForm
from skilllinkapp.models import freelancer


# Create your views here.
def freelancerpanel(request):
    freelancer_id = request.session.get('freelancer_id')

    if not freelancer_id:
        return redirect('freelancerapp:freelancerlogin')

    frln = freelancer.objects.get(id=freelancer_id)

    return render(request, 'freelancer/freelancerpanel.html', {'freelancer': frln})


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
            return render(request, 'freelancer/freelancerlogin.html')

    return render(request, 'freelancer/freelancerlogin.html')

def freelancersignup(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        mobile = request.POST.get('mobile')
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
            mobile=mobile,
            education=education,
            category=category
        )
        new_freelancer.save()

        messages.success(request, "Account created successfully")
        #return redirect('companylogin')

     return render(request, 'freelancer/freelancersignup.html')
 
def manage_profile(request):
    freelancer_id = request.session.get('freelancer_id')

    if not freelancer_id:
        return redirect('freelancerapp:freelancerlogin')

    frln = freelancer.objects.get(id=freelancer_id)

    if request.method == 'POST':
        form = FreelancerProfileForm(request.POST, instance=frln)
        if form.is_valid():
            form.save()
            return redirect('freelancerapp:freelancerpanel')
    else:
        form = FreelancerProfileForm(instance=frln)

    return render(request, 'freelancer/managefreelancer.html', {'form': form, 'freelancer': frln})


from skilllinkapp.models import project  # add this import at top

def find_project(request):
    freelancer_id = request.session.get('freelancer_id')

    if not freelancer_id:
        return redirect('freelancerapp:freelancerlogin')
    frln = freelancer.objects.get(id=freelancer_id)
    # Get search/filter inputs
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')

    projects = project.objects.all()

    if search:
        projects = projects.filter(title__icontains=search) | projects.filter(requiredskills__icontains=search)

    if category:
        projects = projects.filter(title__icontains=category)

    return render(request, 'freelancer/findproject.html', {'projects': projects, 'search': search, 'freelancer': frln})

#freelancer logout view
def freelancerlogout(request):
      request.session.flush()  # clears all session data
      return redirect('freelancerapp:freelancerlogin')


from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from skilllinkapp.models import project, bid, freelancer

def place_bid(request, project_id):
    project_obj = get_object_or_404(project, id=project_id)

    freelancer_id = request.session.get('freelancer_id')
    if not freelancer_id:
        return redirect('freelancerapp:login')

    freelancer_obj = freelancer.objects.get(id=freelancer_id)

    if request.method == 'POST':
        bidamount = request.POST.get('bidamount')
        duration = request.POST.get('duration')
        proposal = request.POST.get('proposal')

       
        if float(bidamount) > project_obj.budget:
            from django.contrib import messages
            messages.error(request, "Bid exceeds project budget")
            return redirect('freelancerapp:placebid', project_id=project_id)

       
        bid.objects.create(
            projectname=project_obj,
            freelancername=freelancer_obj,
            bidamount=bidamount,
            duration=duration,
            proposal=proposal
        )

        return redirect('freelancerapp:freelancerpanel')

    
    return render(request, 'freelancer/placebid.html', {
        'project': project_obj,
        'freelancer': freelancer_obj
    })
    
    
from skilllinkapp.models import bid, allotment

def mybids(request):
    freelancer_id = request.session.get('freelancer_id')
    if not freelancer_id:
        return redirect('freelancerapp:freelancerlogin')

    frln = freelancer.objects.get(id=freelancer_id)
    bids = bid.objects.filter(freelancername=frln)

    bid_list = []
    allocated_count = 0
    pending_count = 0
    rejected_count = 0

    for b in bids:
        allotment_obj = allotment.objects.filter(
            projectname=b.projectname,
            freelancername=frln
        ).first()

        if allotment_obj:
            allocated_count += 1
        elif b.projectname.is_selected:
            rejected_count += 1
        else:
            pending_count += 1

        bid_list.append({
            'bid': b,
            'allotment': allotment_obj,
        })

    return render(request, 'freelancer/mybids.html', {
        'bid_list': bid_list,
        'freelancer': frln,
        'allocated_count': allocated_count,
        'pending_count': pending_count,
        'rejected_count': rejected_count,
    })