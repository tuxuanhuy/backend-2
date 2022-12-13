from django.shortcuts import render

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

from datetime import datetime

# Create your views here.

# List all Employees
class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Get detail of Employee 
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# List all Shifts
class ShiftList(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    # permission_classes = [permissions.IsAuthenticated]


# Search for Shifts in a Date
class ShiftSearch(generics.ListAPIView):
    serializer_class = ShiftSerializer
    
    def get_queryset(self):
        queryset = Shift.objects.all()
        date = self.request.query_params.get('date')
        if date is not None:
            queryset = queryset.filter(date = date)
        return queryset


# Get detail of Shift
class ShiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


# List all Shifts of an Employee
class EmployeeShift(generics.ListAPIView):
    serializer_class = ShiftSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Shift.objects.filter(employee=pk)


# Search for Today
class ShiftToday(generics.ListAPIView):
    serializer_class = ShiftSerializer
    
    def get_queryset(self):
        queryset = Shift.objects.all()
        date = datetime.now().date()
        if date is not None:
            queryset = queryset.filter(date = date)
        return queryset


# Search for Shifts in Range
class ShiftRange(generics.ListAPIView):
    serializer_class = ShiftSerializer

    def get_queryset(self):
        queryset = Shift.objects.all()
        start_time = datetime(2022, 12, 14)
        end_time = datetime(2022, 12, 15)

        queryset = queryset.filter(start_time__range=[start_time, end_time])
        return queryset
