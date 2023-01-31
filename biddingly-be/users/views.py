from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class ProfileAPIView(APIView):
    def get(self, request):
        return Response(UserSerializer(instance=request.user).data)
