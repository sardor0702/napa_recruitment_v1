from rest_framework.views import APIView
from .serializers import UserSerializer
from napa_recruitment.responses import ResponseSuccess

class Me(APIView):
    def get(self, request):
        return ResponseSuccess(UserSerializer(data=request.user).data)