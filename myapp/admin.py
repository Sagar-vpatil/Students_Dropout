from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import StudentsInfo

@admin.register(StudentsInfo)
class StudentsAdmin(ImportExportModelAdmin):
    list_display = ('Student_name','Standard','Aadhaar_no')
    
#admin.site.register(StudentsInfo)

# Register your models here.
