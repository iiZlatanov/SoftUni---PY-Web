from django.shortcuts import render, redirect
#
# from form_basics.web.forms import EmployeeForm
from form_basics.web.forms import EmployeeForm


def index(request):
    form = EmployeeForm(
        request.POST or None,
        initial={
            "lname": "Minkov",
        }
    )

    if request.method == 'POST':
        if form.is_valid():
                print(form.cleaned_data)
                return redirect('index')

    context = {'employee_form': form}

    return render(request, 'web/index.html', context)
#
# def index(request):
#     if request.method == 'GET':
#         context = {
#             "employee_form": EmployeeForm(),
#         }
#
#         return render(request, "web/index.html", context)
#
#     else: # request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         #print(request.POST['first_name'])
#         if form.is_valid():
#             # data is valid, populate 'cleaned_data'
#             print(form.cleaned_data['first_name'])
#             # use the data
#             # redirect to some URL
#             return redirect('index')
#         else:
#             # data is invalid, populate 'errors'
#             context = {
#                 "employee_form": form,
#             }
#
#             return render(request, "web/index.html", context)
