from django.urls import path
from .views import get_names

urlpatterns = [
    path('api/get_names', get_names, name='get_names'),
]