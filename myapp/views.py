from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from .models import StudentsInfo
from .resources import StudentResources
from tablib import Dataset
from django.http import HttpResponse


# Create your views here.


def simple_upload(request):
    if request.method == "POST" :
        student_resource = StudentResources()
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request,'Wrong Format')
            return render(request,'excel.html')
        
        imported_data = dataset.load(new_student.read(),format='xlsx')
        for data in imported_data:
            value = StudentsInfo(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12]
                
            )

            value.save()
        messages.info(request,'Data Uploaded Successfully!')
    return render(request,'excel.html')

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

def Uplod(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'Uplod.html')

    
def form(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'form.html')

       
def URL(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'URL.html')

       
def excel(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'excel.html')


           



