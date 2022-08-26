from email import message
import re
from django.forms import ValidationError
from rest_framework import serializers
from .models import Vehicle
from django.core.validators import RegexValidator

def regex_validator(value,message,regex):
    if len(value) < 0:
        raise ValidationError(f"{message} cannot be empty")
    validator = RegexValidator(rf"{regex}",f"{message} contain only alphanumeric character")
    return validator(value)

class VehicleSerializer(serializers.ModelSerializer):

    def validate_vehicle_number(self, value):
        regex = '^[0-9a-zA-Z]*$'
        field_name = "vehicle_number"
        regex_validator(value,field_name,regex)
        return value
    
    def validate_vehicle_name(self, value):
        regex = '^[0-9a-zA-Z-()]+(\s+[-0-9a-zA-Z-()]+)*$'
        field_name = "vehicle_number"
        regex_validator(value,field_name,regex)
        return value
    
    def validate_vehicle_description(self, value):
        regex = '^[0-9a-zA-Z-()]+(\s+[-0-9a-zA-Z-()]+)*$'
        field_name = "vehicle_number"
        regex_validator(value,field_name,regex)
        return value

    class Meta:
        model = Vehicle
        fields = '__all__'
    