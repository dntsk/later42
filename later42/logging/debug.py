class ExceptionLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.body)
        print(request.scheme)
        print(request.method)
        print(request.META)
        print(request.headers)

        response = self.get_response(request)

        return response