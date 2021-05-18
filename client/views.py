from django.http import HttpResponse
from dashboard.models import loanType
from .models import Loan,Payments
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm,PostForm
from django.shortcuts import render, redirect,get_object_or_404
# Create your views here.

def homepage(request):
    return render (
        request=request,
        template_name="index2.html",
        context={},
    )
def clientpage(request):
    return render (
        request,
        template_name="useraccount.html",
        context={}
    )    
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})                     

def index_loan(request):
        queryset = Loan.objects.all()
        context = {
                "title":"Homepage",
                "Loan_list":queryset
        }
        return render(request, "index1.html",context = {"Loan_list":Loan.objects.all})

#Loans for loan urlMap
def apply_loan(request):
	form = PostForm( request.POST or None )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"form": form,
		"title":"Apply"
	}
	return render(request, "apply.html",context)
#Loan Details
def loan_details(request, id=None):
	instance = get_object_or_404(Loan, id=id)
	context = {
		"title": instance.title,
		"instance":instance
	}
	return render(request, "detail.html", context)
#Loan Types
def loan_types(request):
	context = {
		"title":"Types of loans"
	}
	return render(request, "loantypes.html", 
        context={'loantypes':loanType.objects.all})
#Payments
def payments(request):
	money = Payments.objects.all();
	context = {
		"title":"Payments",
		"money":money
	}
	return render(request, "payments.html",context)
#Employees
def employees(request):
	context = {
		"title":"Employees"
	}
	return render(request, "employees.html",context)
#Company Setup
def company_setup(request):
	context = {
		"title":"Company setup"
	}
	return render(request, "company.html",context)
#Borrowers
def borrowers(request):
	context = {
	 	"title":"Borrowers"
	}
	return render(request, "borrowers.html",context)

#@login_required()
def user_dashboard(request):
    return render(request, 'dashboard.html')

def settings(request):
    return render(request, 'settings1.html')