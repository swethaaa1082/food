from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        username = request.POST['username']
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print("user created")
            return redirect('/')
        else:
                messages.info(request, "password not matched")
                return redirect('register')
    else:
        return render(request,'registration.html')
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')


