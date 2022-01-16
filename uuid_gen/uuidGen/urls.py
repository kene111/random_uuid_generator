from django.urls import path
from .views import *



urlpatterns = [
    path('', Uuid.as_view()),
]  