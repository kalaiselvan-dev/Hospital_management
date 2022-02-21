from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import doctor
from .models import patient
from .serializers import DoctorSerializer
from .serializers import PatientSerializer
from rest_framework import status
from django.db.models import Q
import math


class doctor_list(APIView):
    def get(self, request):
        doctors = doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        s = request.GET.get('s')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page', 1))
        per_page = 32
        doctors = doctor.objects.all()

        if s:
            doctors = doctors.filter(
                Q(name__icontains=s) | Q(email__icontains=s))

        if sort == 'asc':
            doctors = doctors.order_by('name')

        elif sort == 'desc':
            doctors = doctors.order_by('-name')

        total = doctors.count()
        start = (page - 1) * per_page
        end = page * per_page
        serializer_class = DoctorSerializer(doctors[start:end], many=True)
        return Response({'data': serializer_class.data,
                         'total': total,
                         'page': page,
                         'last_page': math.ceil(total / per_page),
                         })


class doctor_details(APIView):
    def get(self, request, pk):
        try:
            doctors = doctor.objects.get(pk=pk)
        except doctor.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctors)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            doctors = doctor.objects.get(pk=pk)
        except doctor.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer(doctors, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            doctors = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        doctors.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class patient_list(APIView):
    def get(self, request):
        patients = patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        s = request.GET.get('s')
        sort = request.GET.get('sort')
        page = int(request.GET.get('page', 1))
        per_page = 32
        patients = patient.objects.all()

        if s:
            patients = patients.filter(
                Q(name__icontains=s) | Q(email__icontains=s))

        if sort == 'asc':
            patients = patients.order_by('name')

        elif sort == 'desc':
            patients = patients.order_by('-name')

        total = patients.count()
        start = (page - 1) * per_page
        end = page * per_page
        serializer_class = PatientSerializer(patients[start:end], many=True)
        return Response({'data': serializer_class.data,
                         'total': total,
                         'page': page,
                         'last_page': math.ceil(total / per_page),
                         })


class patient_details(APIView):
    def get(self, request, pk):
        try:
            patients = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patients)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            patients = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        serializer = PatientSerializer(patients, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            patients = patient.objects.get(pk=pk)
        except patient.DoesNotExist:
            error = {'status': '400', 'message': 'NOT FOUND'}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        patients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
