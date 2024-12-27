from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index_no_template(request, *args, **kwargs):
    content = f"<h1>It works with:<h1/><br/>" + \
              f" args={args} and kwargs ={kwargs},<br/>" + \
              f"path={request.path},<br/>" + \
              f"method={request.method} and<br/>" + \
              f"user={request.user}"


    return HttpResponse(content, status=201)


def index(request, *args, **kwargs):
    context = {}
    return render(request, 'core/index.html', context)
