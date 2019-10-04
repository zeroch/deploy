from rest_framework import serializers
from reserve.models import Doctor, Patient, Appointment

class DoctorSerializer(serializers.ModelSerializer):
    appointments = serializers.PrimaryKeyRelatedField(many = True, read_only=True)
    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):
    appointments = serializers.PrimaryKeyRelatedField(many = True, read_only=True)

    class Meta:
        model = Patient
        fields = "__all__"
    

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"