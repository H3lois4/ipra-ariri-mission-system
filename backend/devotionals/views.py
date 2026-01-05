from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Devotional
from .serializers import DevotionalSerializer


class DevotionalListAPIView(APIView):
    def get(self, request):
        devotionals = Devotional.objects.all().order_by('-created_at')
        serializer = DevotionalSerializer(devotionals, many=True)
        return Response(serializer.data)
