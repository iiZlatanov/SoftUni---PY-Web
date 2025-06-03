import random

from django.shortcuts import render


cat_images = (
    'https://cdn.britannica.com/39/226539-050-D21D7721/Portrait-of-a-cat-with-whiskers-visible.jpg',
    'https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg',
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
        'numbers': [x + 1 for x in range(-10, 10)],
    }
    return render(request, 'web/index.html', context)

def about(request):
    return render(request, 'web/about.html')