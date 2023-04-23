from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), # /challenges
    path('ping', views.ping),
    path("<int:month>", views.monthly_challenge_by_int),
    path("<str:month>", views.monthly_challenges_by_str, name="month-challenge"),
]
