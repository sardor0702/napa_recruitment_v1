from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from .responses import ResponseSuccess

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        data = super(CustomPagination, self).get_paginated_response(data)
        data.data['per_page'] = settings.REST_FRAMEWORK['PAGE_SIZE']
        return ResponseSuccess(data.data)
