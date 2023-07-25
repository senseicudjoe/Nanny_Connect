from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .models import Customuser
# from .models import user


def register(request):
    context = {}
    if request.method=="POST":
        email = request.POST['email'] #getting the email
        fname = request.POST['fname'] #getting the first name
        lname = request.POST['fname'] #getting the last name
        password1 = request.POST['password'] #getting first password
        password2 = request.POST['password2'] #getting second password
        status = request.POST['status']

        # checking if user entered a value for all fields
        if len(email) != 0 and len(fname) != 0 and len(fname) != 0 and len(password1) != 0 and len(password2) !=0 and len(status) !=0:
            # Checking if the confirmation password and the initial password are the same
            if len(fname) <= 10 and len(lname) <=10: 
                if password2==password1:
                    if Customuser.objects.filter(username = email).exists():
                        messages.error(request,"Email already exists! Login")
                    else:
                        # registering the user if email doesn't exist
                        user=Customuser()
                        user.first_name = fname
                        user.last_name = lname
                        user.username = email #setting the username to the email entered
                        user.email = email #setting the email to the email entered
                        user.set_password(password2) #setting the user password to the confirmation password entered
                        if status == "client":
                            user.is_client = True
                        else:
                            user.is_nurse = True
                        user.save() #saving user credentials to database

                        try:
                            auth = authenticate(request, username=email, password=password2) #authenticate user
                            if auth is not None: #if user login credentials are correct
                                login(request,auth) #log user in
                                return redirect("/") #redirect user to user dashboard
                            else: #if user login credentials are incorrect
                                messages.error("Invalid email or password")
                                return redirect("/authApp/login/") #redirect user to login page
                        except Exception as e: #if an unkown error occur
                            print(e) #output error to terminal
                else:
                    messages.error(request,"Passwords do not match")
            else:
                messages.error(request,"Enter a valid first name or last name")
        else:
            messages.error(request,"Make sure all fields have been filled")
    return render(request,'register.html',context)



def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            auth = authenticate(request, username=username, password=password) #authenticate user, returns none if user credentials do not match what is in the database
            print(auth)
            if auth is not None: #if user login credentials are correct
                login(request,auth) #log user in
                return redirect("/") #redirect user to user dashboard
            else: #if user login credentials are incorrect
                messages.error(request,"Incorrect username or password ")
        except Exception as e: #if an unkown error occur
            print(e) #output error to terminal

    return render(request,'login.html',{})





def signout(request):
    logout(request)
    return redirect('../auth/signin')

