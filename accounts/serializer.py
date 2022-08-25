from .models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user_type = validated_data.get('user_type')
        if user_type == 'S':
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
