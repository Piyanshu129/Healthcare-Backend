from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Patient(models.Model):
    created_by = models.ForeignKey(User, related_name="patients", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.id})"

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, related_name="mappings", on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, related_name="mappings", on_delete=models.CASCADE)
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("patient", "doctor")

    def __str__(self):
        return f"Patient {self.patient_id} -> Doctor {self.doctor_id}"
