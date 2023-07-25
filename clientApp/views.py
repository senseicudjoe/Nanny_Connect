from django.shortcuts import render,redirect
from .models import nurse

def home(request):
    
    return render(request,"home.html",{})

def nurses(request):
    all_nurses = nurse.objects.all()
    context = {"all_nurses":all_nurses}

    return render(request,"client_dashboard.html", context)
# Create your views here.
