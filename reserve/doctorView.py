from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from reserve.models import Doctor
from reserve.serializers import DoctorSerializer
from rest_framework import status
from django.http import Http404

class DoctorListView(APIView):
    def get(self, request, format=None):
        doctor = Doctor.objects.order_by('id')
        doc_serializer = DoctorSerializer(doctor, many=True)

        return Response(doc_serializer.data)


    def post(self, request, format=None):
        doc_serializer = DoctorSerializer(data=request.data)
        if doc_serializer.is_valid():
            doc_serializer.save()
            return Response(doc_serializer.data, status=status.HTTP_201_CREATED)
        return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DoctorDetailView(APIView):
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        