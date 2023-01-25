from django.urls import path
from .views import reacharge

urlpatterns = [
    path('', reacharge)
]