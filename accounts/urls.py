from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/',views.RegistrationView.as_view(),name="register"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
