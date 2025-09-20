from rest_framework import routers
from django.urls import path, include
from .views import PatientViewSet, DoctorViewSet, MappingViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'mappings', MappingViewSet, basename='mapping')

urlpatterns = [
    path('', include(router.urls)),
]
