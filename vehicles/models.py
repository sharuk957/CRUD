from django.db import models

# Create your models here.
class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('TW',"Two"),
        ('TH',"Three"),
        ('FO',"Four"),
    ]
    vehicle_number = models.CharField(max_length=10,primary_key=True)
    vehicle_type = models.CharField(max_length=2,choices=TYPE_CHOICES)
    vehicle_name = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.name

