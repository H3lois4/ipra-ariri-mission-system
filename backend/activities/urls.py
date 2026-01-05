from django.urls import path
from .views import activity_summary

urlpatterns = [
    path('summary/', activity_summary, name='activity-summary'),
]
