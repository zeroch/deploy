from django.db import models
from enum import Enum
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    class AppointmentKind(Enum):
        NewPatient = 'NP', _('New Patient')
        FollowUpPatient = 'FU', _('Follow Up')
    
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)


    start_time = models.TimeField()
    event_date = models.DateField()

    
    def __str__(self):
        return "%s %s %s" % (self.doctor, self.start_time, self.event_date)