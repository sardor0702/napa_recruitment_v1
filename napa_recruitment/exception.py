from rest_framework.views import exception_handler



def handler(exc, context):
    response = exception_handler(exc, context)

    detail = None
    if response is not None:
        if response.data is str:
            detail = response.data
        elif "detail" in response.data:
            detail = response.data["detail"]

    if response is None:
        raise exc

    response.data = {
        "status": "error",
        "data": detail
    }

    return response
