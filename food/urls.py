from django.urls import path

from . import views

app_name = 'food'

urlpatterns = [
    path("contact/", views.contact, name="contact"),
    path("pizza/", views.pizza, name="pizza"),
    path("burgers/", views.burgers, name="burgers"),
]