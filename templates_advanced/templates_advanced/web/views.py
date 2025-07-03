import random

from django.shortcuts import render

cat_images = (
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZgX_lhpIZzVFs0vDnLmTxDLAk0uW9sNAFJQ&s',
    'https://cdn.hswstatic.com/gif/shutterstock-698651233-hero.jpg',
)

cat_names = (
    'Pepelyashka',
    'GoSho',
)

def index(request):
    index = random.randint(0, len(cat_images) - 1)
    context = {
        'cat_image': cat_images[index],
        'cat_name': cat_names[index],
    }
    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')
