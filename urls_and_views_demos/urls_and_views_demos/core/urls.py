from django.urls import path

from urls_and_views_demos.core.views import index, redirect_to_softuni, redirect_to_index, redirect_to_index_with_params

urlpatterns = (
    path('to-softuni/', redirect_to_softuni),
    path('to-index/', redirect_to_index, name='redirect_to_index'),
    path('to-index-with-params/', redirect_to_index_with_params, name='redirect_to_index_with_params'),

    path('', index, name='index_no_params'),
    path('<int:pk>/', index),
    path('<slug:slug>/', index),
    path('<int:pk>/<slug:slug>/', index, name='index_with_pk_and_slug'),
)
