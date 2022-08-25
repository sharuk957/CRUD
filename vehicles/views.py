from django.shortcuts import render
from rest_framework import viewsets
from .serializer import VehicleSerializer
from .models import Vehicle
from rest_framework import permissions
from accounts.permission import IsSuperUser


class VehiclesCRUDOperationView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]