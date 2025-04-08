import random

from django.shortcuts import render

cats = [
    'https://cdn.britannica.com/39/226539-050-D21D7721/Portrait-of-a-cat-with-whiskers-visible.jpg',
    'https://lacvets.com/wp-content/uploads/2023/01/what-is-a-cats-lifespan-lakeland-fl-scaled.jpg',
]


def index(request):
    context = {
        'cat_image': random.choice(cats),
    }

    return render(request, 'web/index.html', context)


def about(request):
    return render(request, 'web/about.html')
