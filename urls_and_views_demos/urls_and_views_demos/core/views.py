from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request, *args, **kwargs):
    content = f"It works with:<br/>" + \
              f" args={args} and kwargs ={kwargs},<br/>" + \
              f"path={request.path},<br/>" + \
              f"method={request.method} and<br/>" + \
              f"user={request.user}"


    return HttpResponse(content, status=201)

