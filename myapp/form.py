from django import forms
from .models import StudentsInfo

class StudentData(forms.Form):
	class Meta:
		model = StudentsInfo
		fields = '__all__'