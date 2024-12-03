def measure_time(get_response):
    def middleware(request, *args, **kwargs):
        print('Before view')
        result = get_response(request, *args, **kwargs)
        print('After view')
        return result

    return middleware
