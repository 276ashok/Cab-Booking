from django.shortcuts import render
from .forms import *

# Create your views here.


def cabdrive_login(request):
    return render(request, 'cabdrivers/cabdrivers_login.html')


def driver_signup(request):
    form = Driver_Signup_form()
    if request.method == "POST":
        form = Driver_Signup_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'cabdrivers/driver_signup.html', {"form": form})
