from django.shortcuts import render, redirect
from django.http import HttpResponse
from cabriders.models import cabriders_signup

# Create your views here.


def home(request):
    return render(request, 'cabriders/home.html')


def login(request):
    if request.method == "POST":
        verify_auth = cabriders_signup.objects.get(Email = request.POST.get('rider_username'), Password = request.POST.get('rider_pass'))
        return redirect('map')
    return render(request, 'cabriders/login.html')

def map(request):
    return render(request,'cabriders/map.html')