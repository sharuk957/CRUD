from django.shortcuts import render
from .models import User
from .serializer import RegistrationSerializer
from rest_framework import generics,views,status,response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrationView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class LoginView(views.APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        if User.objects.filter(email=email).first():
            user = authenticate(email=email,password=password)

            if user is None:
                return response.Response({'message':'invalid Credential'},status=status.HTTP_401_UNAUTHORIZED)
        else:
            return response.Response({'message':'Invalid email'},status=status.HTTP_401_UNAUTHORIZED)
        refresh = RefreshToken.for_user(user)
        return response.Response({
            "refresh": str(refresh),
        'access': str(refresh.access_token)
        })

