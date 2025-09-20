from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: SAFE methods allowed; modifications only by owner (created_by).
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, "created_by", None) == request.user

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by("-created_at")
    serializer_class = DoctorSerializer

    def get_permissions(self):
        # Anyone can view (list/retrieve). Only authenticated users can create/update/delete.
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only mappings for patients created by the requesting user
        return PatientDoctorMapping.objects.filter(patient__created_by=self.request.user).select_related("patient", "doctor")

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        patient_id = data.get("patient")
        doctor_id = data.get("doctor")

        if not patient_id or not doctor_id:
            return Response({"detail": "patient and doctor fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        patient = get_object_or_404(Patient, id=patient_id)
        if patient.created_by != request.user:
            return Response({"detail": "You can only assign doctors to patients you created."}, status=status.HTTP_403_FORBIDDEN)

        # ensure doctor exists
        get_object_or_404(Doctor, id=doctor_id)

        data["assigned_by"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"], url_path=r"patient/(?P<patient_id>\d+)")
    def get_doctors_for_patient(self, request, patient_id=None):
        patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
        mappings = self.get_queryset().filter(patient=patient)
        doctors = [m.doctor for m in mappings]
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
