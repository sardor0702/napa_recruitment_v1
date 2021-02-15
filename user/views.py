from rest_framework.views import APIView
from .serializers import UserSerializer, RegistrationSerializer
from napa_recruitment.responses import ResponseSuccess, ResponseFile


class Me(APIView):
    def get(self, request):
        return ResponseSuccess(UserSerializer(data=request.user).data)


class Registration(APIView):
    def post(self, request):
        data = RegistrationSerializer(data=request.data)
        if not data.is_valid():
            return ResponseFile(data.data)

        return ResponseSuccess("ok")
