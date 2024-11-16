from rest_framework.views import exception_handler

def CustomExHandler(exe, context):
    response = exception_handler(exe, context)

    if response:
        
        data = {
            "status_code": response.status_code,
            "watermark": "Habijabi",
            "description": response.data.get('detail', None)
        }

        response.data = data

    return response