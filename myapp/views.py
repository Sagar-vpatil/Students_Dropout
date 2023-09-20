from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib import messages
from .models import StudentsInfo
from .resources import StudentResources
from tablib import Dataset
from django.http import HttpResponse
#Rushwan Scrapdata
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from django.utils.formats import get_format
from django.utils import formats


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
                data[12],
                data[13],
                data[14]
                
            )

            value.save()
        messages.info(request,'Data Uploaded Successfully!')
    return render(request,'excel.html')

def index(request):
    if request.user.is_anonymous :
        return redirect("/login")
    #Queries-Gender
    Male_no = StudentsInfo.objects.filter(Gender='Male').count()
    Male_no = int(Male_no)
   
    Female_no= StudentsInfo.objects.filter(Gender='Female').count()
    Female_no = int(Female_no)
    
    Other = StudentsInfo.objects.filter(Gender='Other').count()
    Other = int(Other)

    gender_list = ['Male','Female','Other']
    gender_number =[Male_no,Female_no,Other]

    #Queries-Cast
    obc = StudentsInfo.objects.filter(Cast='OBC').count()
    obc = int(obc)

    Open = StudentsInfo.objects.filter(Cast='Open').count()
    Open = int(Open)

    St = StudentsInfo.objects.filter(Cast='ST').count()
    St = int(St)

    Sc = StudentsInfo.objects.filter(Cast='SC').count()
    Sc= int(Sc)

    cast_list =['Open','OBC','SC','ST']
    cast_number =[Open,obc,Sc,St]

    #Queries-District
    ahmedabad= StudentsInfo.objects.filter(District='Ahmedabad').count()
    ahmedabad = int(ahmedabad)

    surat = StudentsInfo.objects.filter(District='Surat').count()
    surat = int(surat)

    bhavnagar = StudentsInfo.objects.filter(District='Bhavnagar').count()
    bhavnagar = int(bhavnagar)

    bharuch = StudentsInfo.objects.filter(District='Bharuch').count()
    bharuch = int(bharuch)

    district_list =['Ahmedabad','Bhavnagar','Surat','Bharuch']
    district_number=[ahmedabad,bhavnagar,surat,bharuch]

    total_students = StudentsInfo.objects.count()
    


    context = {
        'gender_list':gender_list,
        'gender_number':gender_number,
        'cast_list':cast_list,
        'cast_number':cast_number,
        'district_list':district_list,
        'district_number':district_number,
        'total_students':total_students

    }

    return render(request,'index.html',context)

def flot(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'flot.html')

def morris(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'morris.html')
    
def chartjs(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'chartjs.html')

def chartist(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'chartist.html')

def sparkline(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'sparkline.html')

def peity(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'peity.html')


def Format(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'Format.html')



def loginUser(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged Successfully!")
            return redirect("/Uplod")
    
        else:
            messages.success(request, "Please Enter Valid Password And Unsername!")
            return render(request,'login.html')
        


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return render(request,'login.html')

def Uplod(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'Uplod.html')

    
def form(request):
    if request.method == "POST" :
         student_name = request.POST.get('Sname')
         standard = request.POST.get('standard')
         aadhaar_no= request.POST.get('aadhaar')
         age = request.POST.get('age')
         cast = request.POST.get('cast')
         phone = request.POST.get('phone')
         address = request.POST.get('address')
         city = request.POST.get('city')
         district = request.POST.get('district')
         state = request.POST.get('state')
         gender = request.POST.get('gender')
         reason = request.POST.get('reason')
         school_name = request.POST.get('school_name')
         leaving_date = request.POST.get('leave_date')
         students_info = StudentsInfo(Student_name=student_name,Standard=standard,Aadhaar_no=aadhaar_no,Age=age,Cast=cast,Phone=phone,
           Address=address,City=city,District=district,State=state,Gender=gender,Reason=reason,School_name=school_name,Leaving_date=leaving_date)
         students_info.save()
         messages.success(request, "Student data has been submited!")
         return render(request,'form.html')
         


    return render(request,'form.html')

       
#def URL(request):
    #if request.user.is_anonymous :
        #return redirect("/login")
    #return render(request,'URL.html')

       
def excel(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'excel.html')


#Rushwan Scrapdata
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def URL(request):
    if request.method == 'POST':
        url_to_check = request.POST.get('url')
        if url_to_check:
            url_validator = URLValidator()
            try:
                url_validator(url_to_check)
                req = requests.get(url_to_check)
                soup = BeautifulSoup(req.content, "html.parser")

                table = soup.find('table')
                rows = table.find_all('tr')
                for row in rows[1:]:  # Skip the header row if present
                    columns = row.find_all('td')
                    Student_name = columns[0].text.strip()
                    standard = columns[1].text.strip()
                    aadhaar_no = columns[2].text.strip()
                    age = columns[3].text.strip()
                    cast = columns[4].text.strip()
                    phone = columns[5].text.strip()
                    address = columns[6].text.strip()
                    city = columns[7].text.strip()
                    district = columns[8].text.strip()
                    state = columns[9].text.strip()
                    gender = columns[10].text.strip()
                    reason = columns[11].text.strip()
                    school_name = columns[12].text.strip()
                    leaving_date = columns[13].text.strip()
                   
                    StudentsInfo.objects.create(Student_name=Student_name,Standard =standard,Aadhaar_no=aadhaar_no,Age=age,Cast=cast,Phone=phone, Address=address,City=city,District=district,State=state,Gender=gender,Reason=reason,School_name=school_name,Leaving_date=leaving_date)
                    

                messages.success(request,"Upload Successfully")

            
            except ValidationError as e:

                error_message = "Invalid URL provided."
                messages.warning(request,error_message)

        else:
            error_message = "Please provide a URL."
            messages.warning(request,error_message)
    return render(request, 'URL.html')


           



