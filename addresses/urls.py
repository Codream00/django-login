from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    path("", views.address_list),
    path("login/", views.login),
    path("<int:pk>/", views.address),
]
