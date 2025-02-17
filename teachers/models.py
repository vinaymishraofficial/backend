from django.db import models

# Create your models here.

class Teacher(models.Model):
    serial_no = models.IntegerField(blank=True, null=True)
    teacherName = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    dateOfBirth = models.CharField(max_length=30, blank=True, null=True)
    teachingExperience = models.TextField(blank=True, null=True)
    ftgt = models.TextField(blank=True, null=True)
    registrationNumber = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.teacherName}"

class UniversityAffiliation(models.Model):
    image = models.ImageField(upload_to='media/Universityimages/', blank=True, null=True)
    alt = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.alt}"