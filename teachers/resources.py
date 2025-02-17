# filepath: /f:/Projects/Django Api Project/Django Api/backend/teachers/resources.py
from import_export import resources # type: ignore
from .models import teacher ,universityAffiliation

class TeacherResource(resources.ModelResource):
    class Meta:
        model = teacher

class UniversityAffiliationResource(resources.ModelResource):
    class Meta:
        model = universityAffiliation
    