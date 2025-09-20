from rest_framework import serializers
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.id')

    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ("created_by", "created_at")

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = ("created_at",)

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = "__all__"
        read_only_fields = ("assigned_by", "assigned_at")
