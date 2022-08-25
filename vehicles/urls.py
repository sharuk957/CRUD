from xml.etree.ElementInclude import include
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('',views.VehiclesCRUDOperationView,basename='vehicle')
urlpatterns = [
    path('api/vehicles/',include(router.urls)),
]
