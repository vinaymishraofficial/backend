from django.contrib import admin
from .models import Teacher, UniversityAffiliation
from import_export.admin import ImportExportModelAdmin # type: ignore

# Register your models here.

class TeacherAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(UniversityAffiliation)