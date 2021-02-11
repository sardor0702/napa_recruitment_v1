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
    ])
