from .models import User
from rest_framework import serializers
from napa_recruitment.validators import PhoneValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name')




class RegistrationSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15, validators=[
        PhoneValidator()
    ], required=True)


    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def validate_first_name(self, value):
        raise ValueError("nice")
