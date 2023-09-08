from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
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

def login(request):
    return render(request,'login.html')


