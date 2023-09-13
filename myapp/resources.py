from import_export import resources
from .models import StudentsInfo

class StudentResources(resources.ModelResource):
    class Meta:
        model = StudentsInfo