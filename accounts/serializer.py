from unittest.util import _MAX_LENGTH
from .models import User
from rest_framework import serializers
from django.core.validators import RegexValidator
from django.forms import ValidationError


def name_validator(value,message):
    if len(value) < 0:
        raise ValidationError(f"{message} cannot be empty")
    validator = RegexValidator(r'^[a-zA-Z]*$',f"{message} contain only character")
    return validator(value)


def email_validator(value,message):
    if len(value) < 0:
        raise ValidationError(f"{message} cannot be empty")
    validator = RegexValidator(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',f"invalid {message} format")
    return validator(value)


def password_validator(value,message):
    if len(value) < 0:
        raise ValidationError(f"{message} cannot be empty")
    validator = RegexValidator(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{5,}$',f"{message} contain Minimum five characters, at least one letter, one number and one special character:")
    return validator(value)


class RegistrationSerializer(serializers.ModelSerializer):

    def validate_email(self,value):
        email_validator(value,'email')
        return value
    
    def validate_first_name(self,value):
        name_validator(value,'first_name')
        return value

    def validate_last_name(self,value):
        name_validator(value,'last_name')
        return value

    def validate_password(self,value):
        password_validator(value,'password')
        return value
    
    class Meta:
        model = User
        fields = ['user_type', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user_type = validated_data.get('user_type')
        if user_type == 'S':
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
