from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def index(request):
    #if request.user.is_anonymous :
        #return redirect("/login")
    return render(request,'index.html')

def flot(request):
    return render(request,'flot.html')

def morris(request):
    return render(request,'morris.html')
    
def chartjs(request):
    return render(request,'chartjs.html')

def chartist(request):
    return render(request,'chartist.html')

def sparkline(request):
    return render(request,'sparkline.html')

def peity(request):
    return render(request,'peity.html')

def loginUser(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged Successfully!")
            return redirect("/")
    
        else:
            messages.success(request, "Please Enter Valid Password And Unsername!")
            return render(request,'login.html')
        


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'index.html')


