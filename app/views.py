from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import * 
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.


def createPage(request):
    form = CreateUserForm()
    if request.method== "POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            group = Group.objects.get(name= 'customer')
            user.groups.add(group)
            return redirect('login')
    context= {'form':form}
    return render(request, "signup.html")
    
def loginPage(request):

    if request.method== "POST":
        email= request.POST.get("email")
        password= request.POST.get("password")

        user= authenticate(request, email= email, password= password)
        if user is not None:
            login(request, user)
            return redirect("home")

        
        

    context= { }
    return render(request, 'login.html' ,context)

def logoutUser(request):

    logout(request)
    return redirect("login")


@login_required(login_url= "login")
@admin_only
def home(request):
    context= {}
    return render(request, 'home.html' ,context)


