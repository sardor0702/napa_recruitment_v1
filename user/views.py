from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

class Me(APIView):
    def get(self, request):
        return Response(UserSerializer(data=request.user).data)