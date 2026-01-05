from django.urls import path
from .views import ExpenseListCreateAPIView

urlpatterns = [
    path('', ExpenseListCreateAPIView.as_view()),
]
