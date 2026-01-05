from django.urls import path
from .views import ActivitySummaryAPIView, ActivityListCreateAPIView

urlpatterns = [
    path('summary/', ActivitySummaryAPIView.as_view(), name='activity-summary'),
    path('', ActivityListCreateAPIView.as_view(), name='activity-list-create'),
]
