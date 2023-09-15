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
                # for re in soup(["thead"]):
                #     re.extract()
                # for script in soup(["script", "style", "title", "head", "form", 'meta', '[document]']):
                #     script.extract()
                # res = soup.table.text
                # print(res)

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
                    print(leaving_date)
                    # df = DateFormat(date)
                    # formatted_datetime = formats.date_format(df, "%d-%m-%Y")
                    # # Df = df.format(get_format('DATE_FORMAT'))
                    # print(formatted_datetime)
                    StudentsInfo.objects.create(Student_name=Student_name,Standard =standard,Aadhaar_no=aadhaar_no,Age=age,Cast=cast,Phone=phone, Address=address,City=city,District=district,State=state,Gender=gender,Reason=reason,School_name=school_name,Leaving_date=leaving_date)
                    print(school_name, city, Student_name, state, leaving_date, reason, phone)

                # for row in rows:
                #     th = row.find_all('th')
                #     columns = row.find_all('td')
                #     for i in th:
                #         if i.text == "First":
                #             n = len(i)
                #         elif i.text == "Last":
                #             a = len(i)
                #             print(a)
                # print(n, a)
                # for row in rows[1:]:
                #     th = row.find_all('th')
                #     columns = row.find_all('td')
                #     name = columns[a].text.strip()
                #     address = columns[n].text.strip()
                #     print(name, address, a)



            except ValidationError as e:

                error_message = "Invalid URL provided."
                print(error_message)

        else:
            error_message = "Please provide a URL."
            print(error_message)
    return render(request, 'URL.html')


           



