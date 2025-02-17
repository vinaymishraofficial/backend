from django.urls import path, include
from rest_framework.routers import DefaultRouter #type: ignore
from .views import TeacherViewSet
from .views import UniversityAffiliationViewSet

router = DefaultRouter()
router.register(r'teachers', TeacherViewSet)
router.register(r'university-affiliations', UniversityAffiliationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]