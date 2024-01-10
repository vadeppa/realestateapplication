from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
 
# def custom_login(request):
#     template_name = 'login.html'
#     form = CustomAuthenticationForm(request.POST or None)

#     if request.method == 'POST' and form.is_valid():
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             login(request, user)
#             # Redirect to the 'create_property_unit' page upon successful login
#             return redirect('create_property_unit/')  # Assuming 'create_property_unit' is the name of your URL pattern
#         else:
#             # Handle invalid login credentials
#             messages.error(request, 'Invalid email or password')

#     return render(request, template_name, {'form': form})




 
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')
 
def custom_signup(request):
    template_name = 'signup.html'
    form = CustomUserCreationForm(request.POST or None)
 
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)

        form = CustomUserCreationForm()
        # Redirect to the desired page upon successful signup
        return redirect('/login/')  # Update with your desired redirect page
 
    return render(request, template_name, {'form': form})

def baseview(request):
    return render(request,'navbar.html')

from django.shortcuts import render, redirect
from .models import PropertyUnit, Tenant, Lease
from .forms import PropertyUnitForm, TenantForm, LeaseForm

# @login_required(login_url='/login/')
@login_required(login_url='/login/')
def create_property_unit(request):
    template_name = 'propertyunit_form.html'
    
    if request.method == 'POST':
        form = PropertyUnitForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('/success/')  # Update with your success URL
    else:
        form = PropertyUnitForm()

    return render(request, template_name, {'form': form})
@login_required(login_url='/login/')
def create_tenant(request):
    template_name = 'tenant_form.html'
    
    if request.method == 'POST':
        form = TenantForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/lease-list/')  # Update with your success URL
    else:
        form = TenantForm()

    return render(request, template_name, {'form': form})
@login_required(login_url='/login/')
def create_lease(request):
    template_name = 'lease_form.html'
    
    if request.method == 'POST':
        form = LeaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leas_success')  # Update with your success URL
    else:
        form = LeaseForm()

    return render(request, template_name, {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/login/')

def success(request):
    
    return render(request,'success.html')
@login_required(login_url='/login/')
def property_all(request):
    obj = PropertyUnit.objects.all()
    return render(request,'property_all.html',{'obj':obj})

from django.shortcuts import render, get_object_or_404

def unit_details(request, property_unit_id):
    property_unit = get_object_or_404(PropertyUnit, id=property_unit_id)
    return render(request, 'unit_details.html', {'property_unit': property_unit})
def leas_success(request):
    return render(request,'lease_seucess.html')

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
def sign(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account Created Successfully !!')
            return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def logins(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/create_property_unit/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/')
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')