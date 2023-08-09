import os
from django.contrib import messages # importing error messages for error handling
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render,redirect

from authApp.models import Customuser
from .models import nurse, Request, client
from datetime import date

def home(request):
    
    return render(request,"home.html",{})

def nurses(request):
    all_nurses = nurse.objects.all()
    
    if request.method == "POST" and "filter" in request.POST:
        state = request.POST['state']
        min = request.POST['min']
        max = request.POST['max']
        all_nurses = nurse.objects.filter(city = state).filter(rate__lte = max ).filter(rate__gte = min) # the lte you see in this line of code represents less than or equal to. 
        # So the rate__lte = max refers to nurse rates less than or equal to max.
        if all_nurses == None:
            messages.error(request,"Search result does not match any filter")
            
    elif request.method =="POST" and 'duration' in request.POST:

        start_date = request.POST.get("startdate")
        end_date = request.POST["enddate"]
        id_nurse = request.POST["IDS"]
        id_email = request.user.email
        Client = client.objects.get(email = id_email)#get the user(client) who made the request since only clients will be allowed to access this page
        Nurse = nurse.objects.get(id = id_nurse)
        # # print(Nurse)
        # print(Client)
        # print(id_email)
        x = Request()
        x.start_date = start_date
        x.end_date = end_date
        x.nurse = Nurse
        x.client = Client
        x.save()        





    context = {
        "all_nurses":all_nurses,
        # "age":age
    }



    return render(request,"client_dashboard.html", context)

# Create your views here.
