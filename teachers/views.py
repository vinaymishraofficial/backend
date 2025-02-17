from django.shortcuts import render
from rest_framework import viewsets # type: ignore
from .models import Teacher, UniversityAffiliation
from .serializers import TeacherSerializer, UniversityAffiliationSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class UniversityAffiliationViewSet(viewsets.ModelViewSet):
    queryset = UniversityAffiliation.objects.all()
    serializer_class = UniversityAffiliationSerializer