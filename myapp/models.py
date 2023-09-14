from django.db import models

# Create your models here.

class StudentsInfo(models.Model):
    Student_name = models.CharField(max_length=200,blank=True)
    Standard = models.CharField(max_length=50)
    Aadhaar_no = models.IntegerField()
    Age = models.IntegerField()
    Cast = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    Address = models.TextField(max_length=500)
    City = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Reason = models.TextField()
    School_name = models.CharField(max_length=100,default='Not Available')
    Leaving_date = models.CharField(max_length=30,default='Not Available')
