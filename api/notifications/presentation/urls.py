from django.urls import path
from .views import post_notifications

urlpatterns = [
    path('', post_notifications),
]
