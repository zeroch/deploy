from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from reserve.models import Appointment, Doctor
from reserve.serializers import AppointmentSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from datetime import datetime
from django.db.models import Q

class AppointmentListView(APIView):
    def get(self, request, format=None):
        appointment = Appointment.objects.order_by('id')
        app_serializer = AppointmentSerializer(appointment, many=True)

        return Response(app_serializer.data)


    def post(self, request, format=None):
        if isTimeSlotAvailable(request):
            app_serializer = AppointmentSerializer(data=request.data)
            if app_serializer.is_valid():
                app_serializer.save()
                return Response(app_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("This time Slot is not available", status= status.HTTP_409_CONFLICT)

 
def _getListByDoctorWithinDay(request,pk, format=None):
    doc_id = pk
    date = request.data["event_date"]
    print("date")
    appointments = Appointment.objects.filter(doctor__pk = doc_id, event_date = date)
    app_serializer = AppointmentSerializer(appointments, many=True)
    return app_serializer

def _getListByDoctor(request,pk, format=None):
    appointments = Appointment.objects.filter(doctor__pk = pk)
    app_serializer = AppointmentSerializer(appointments, many=True)
    return app_serializer

def isTimeSlotAvailable(request):
    new_date = request.data["event_date"]
    new_start = datetime.strptime(request.data["start_time"], "%H:%M")
    if new_start.minute % 15 != 0:
        return False
    print("start: " + str(new_start) +  " date: " + str(new_date))
    appointments = Appointment.objects.filter(doctor__pk = request.data["doctor"])
    print("appointments: ", appointments)
    print("doctor: ", request.data["doctor"])
    testing = appointments.filter(Q(start_time= new_start),  Q(event_date= new_date))
    print(appointments, testing, appointments.count(), testing.count())
    return testing.count() < 3


@api_view()
def getListByDoctor(request, pk, format=None):
    app_serializer = _getListByDoctorWithinDay(request, pk, format)
    return Response(app_serializer.data)

        

class AppointmentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Appointment.objects.get(pk=pk)
        except Appointment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = AppointmentSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = AppointmentSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
