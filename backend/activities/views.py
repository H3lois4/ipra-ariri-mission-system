from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

from .models import Activity, ActivityType
from .serializers import ActivitySerializer


class ActivitySummaryAPIView(APIView):
    def get(self, request):
        data = (
            ActivityType.objects
            .annotate(total=Count('activities'))
            .values('id', 'name', 'total')
            .order_by('name')
        )
        return Response(data)


class ActivityListCreateAPIView(APIView):
    def get(self, request):
        activities = Activity.objects.select_related('activity_type', 'created_by')
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
