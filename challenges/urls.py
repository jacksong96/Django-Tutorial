from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:monthly>", views.monthly_challenge_int),
    path("<str:monthly>", views.monthly_challenge, name="monthly-challenge")
]