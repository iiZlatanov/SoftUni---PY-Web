from django.urls import path

from urls_and_views_demos.core.views import index

urlpatterns = (
    path('', index),
)
