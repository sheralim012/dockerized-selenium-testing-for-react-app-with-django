from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import ProfileAPIView


urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]
