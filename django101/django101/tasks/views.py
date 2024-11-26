from django import http
from django.shortcuts import render

from django101.tasks.models import Task
'''
#FBV:
1. A function that has one or more params
2. Returns a response

'''

# def index(request):
#     name = request.GET.get('name', 'NONAME')
#
#     content = "<h1>It works!</h1>" + \
#         f"<p>You are welcome to my project, {name}!</p>" + \
#         "<ul><li>1</li><li>2</li></ul>"
#
#     return http.HttpResponse(content)
#         # headers={
#         #     "Content-Type": "application/json",
#         # }

def index(request):
   tasks = Task.objects.all()

   if not tasks:
       return Http.HttpResponse('<h1>No tasks!!!</h1>')

   result = []

   for task in tasks:
       result.append(f"""
    <li>
        <h2>{task.title}</h2>
        <p>{task.description}</p> 
    </li>
            """)

       ul = f"<ul>{''.join(result)}</ul>"

       content = f"""
       <h1>{len(tasks)}Tasks</h1>
       {ul}
        """

    return Http.HttpResponse(content)
