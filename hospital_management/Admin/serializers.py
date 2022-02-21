from rest_framework import serializers
from .models import doctor
from .models import patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = "__all__"
