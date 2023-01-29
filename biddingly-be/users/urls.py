from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import MeAPIView


urlpatterns = [
    path('token/', obtain_auth_token, name='token'),
    path('me/', MeAPIView.as_view(), name='me'),
]
