from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User 
from .forms import UserForm
def my_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    else:
       
        return render(request,'users/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        
        user=User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
        user.save()
        return redirect('index')
    else:    
        form=UserForm()
    
    context =  {'form':form  }
    return render(request,'users/register.html', context)


