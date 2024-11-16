def simple_middleware(get_response):
    def middleware(request):
        print("Before View Middleware")
        response = get_response(request)
        print("After View Middleware")
        return response

    return middleware