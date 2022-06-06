from django.core.exceptions import ValidationError
from user.models import User


class PhoneValidatorTest:
    requires_context = False

    def __call__(self, value):
        if not User.objects.filter(phone=value).exists():
            raise ValidationError("Этот номер телефона не существует!")