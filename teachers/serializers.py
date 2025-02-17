from rest_framework import serializers  # type: ignore
from .models import Teacher, UniversityAffiliation

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class UniversityAffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversityAffiliation
        fields = '__all__'
