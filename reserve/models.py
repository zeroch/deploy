from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, related_name='appointments', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ['doctor', 'start_time', 'end_time']
    
    def __str__(self):
        return "%s %s %s" % (self.doctor, self.start_time, self.end_time)