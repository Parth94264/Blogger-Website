# Create your views here.
from collections import UserDict
from datetime import timezone
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from blog.models import *
    

def register(request):
    
    if request.method == "POST":
        print("condition true")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email_id = request.POST.get('email_id')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "User Already Exists")
            return redirect('/register/')
        
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email_id,
            
        )
        Blogger.objects.create(user=user)
        
        user.set_password(password)

        user.save()
        messages.info(request, "Registration Completed Sucessfully")
        return redirect("/login/")
        
    
    return render(request, 'account/register.html')



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        user = authenticate(username = username, password = password)
        if user is None :
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else :
            auth_login(request, user)
            return redirect('/')
        
        
    return render(request, "account/login.html")

def logout_page(request):
    auth_logout(request)
    return redirect('/login/')
