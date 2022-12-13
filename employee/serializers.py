from rest_framework import serializers
from .models import Employee, Shift

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id', 
            'full_name', 
            'email', 
            'contact', 
            'address', 
            'picture', 
            'username',
            'password'
        ]

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            'id', 
            'name', 
            'start_time', 
            'end_time', 
            'date',
            'status',
            'employee'
        ]