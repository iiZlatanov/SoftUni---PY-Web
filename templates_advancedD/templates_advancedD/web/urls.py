from django.urls import path

from templates_advancedD.web.views import index, about

urlpatterns = (
    path("", index, name="index"),
    path("about/", about, name="about"),
)