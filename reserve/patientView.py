from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from reserve.models import Patient
from reserve.serializers import PatientSerializer
from rest_framework import status
from django.http import Http404

class PatientListView(APIView):
    def get(self, request, format=None):
        patient = Patient.objects.order_by('id')
        doc_serializer = PatientSerializer(patient, many=True)

        return Response(doc_serializer.data)


    def post(self, request, format=None):
        patient_serializer = PatientSerializer(data=request.data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
        return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PatientDetailView(APIView):
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        patient = self.get_object(pk)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        