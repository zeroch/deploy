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
        fields = ('doctor','start_time','event_date', 'kind', 'patient')

    def to_representation(self, instance):
        rep = super(AppointmentSerializer, self).to_representation(instance)
        rep['kind'] = instance.get_kind_display()
        rep['patient'] = instance.patient.last_name + " " + instance.patient.first_name
        return rep