from django.shortcuts import render


def index(request):
    context = {
        "title": "Employees list",
        "new.employee": "Doncho", # invalid
        "new employee": "Doncho", # invalid
        "123": "456", # invalid
        "1as": "567", # valid
        "_1as": "567", # invalid
        "person": {
            "first_name": "Doncho",
            "last_name": "Minkov",
        },
    }

    return render(request, 'employees/index.html', context)
