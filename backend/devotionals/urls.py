from django.urls import path
from .views import DevotionalListAPIView

urlpatterns = [
    path('', DevotionalListAPIView.as_view()),
]
