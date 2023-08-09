from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import nurse,Customuser
from django.contrib import messages



def nurse_settings(request):
    nurse_details = nurse.objects.get(email = request.user.email)
    # since we created a signal that auto-populates the nurse of client model depending on the status the user,
    # we are using the email field as the point of reference since the nurse model and client model both share the same email as the user email
    return render( request,"nurse_setting.html",{"details": nurse_details})


def updaterecord(request, id):
    if "my_account" in request.POST:
        first_name = request.POST["fname"] 
        last_name= request.POST["lname"]
        number= request.POST["contact"]
        update_nurse = nurse.objects.get(id=id) # since the view rendering before this one is the nurse settings and the nurse object with email = user.email has been passed as a context.
        # the same nurse id is what is being passed into the url for the id for the update record
        update_user = Customuser.objects.get(email = request.user.email) # getting the same user object who is logged in so that we can change the details
        update_nurse.fname = first_name
        update_user.first_name = first_name
        update_nurse.lname = last_name
        update_user.last_name = last_name
        update_nurse.phone = number
        update_nurse.save()
        update_user.save()
        return HttpResponseRedirect(reverse('nurse_settings'))
    
    if "security" in request.POST:
        old_password = request.POST["old_password"]
        new_password1 = request.POST["new_password1"]
        new_password2 = request.POST["new_password2"]
        user = Customuser.objects.get(id = request.user.id)
        if user.check_password(old_password):
            if new_password1 == new_password2:
                user.set_password(new_password2)
                # note that using the set password automatically logs you out, hence the reason I am redirecting to the login page.
                user.save()    
                messages.info(request,"Password successfully changed")
                return HttpResponseRedirect(reverse('signin'))
            else:
                messages.error(request,"Passwords do not match")
        else:
            messages.error(request,"Old password did not match password")

    if "my_profile" in request.POST:
        rate = request.POST["rate"]
        bio = request.POST["bio"]
        city = request.POST["city"]

        if not request.POST["nurse_CV"]:
            print("summer")
            update_nurse = nurse.objects.get(id=id)
            update_nurse.rate = rate
            update_nurse.bio = bio
            update_nurse.city = city
            update_nurse.save()
            return HttpResponseRedirect(reverse('nurse_settings'))
        else:
            print("winter")
            qualification = request.FILES["nurse_CV"]
            update_nurse = nurse.objects.get(id=id)
            update_nurse.rate = rate
            update_nurse.bio = bio
            update_nurse.city = city
            update_nurse.qualification = qualification
            update_nurse.save()
            return HttpResponseRedirect(reverse('nurse_settings'))
        # breakpoint()

def manage_jobs(request):
    return render(request,"manage-jobs.html",{})
# Create your views here.    