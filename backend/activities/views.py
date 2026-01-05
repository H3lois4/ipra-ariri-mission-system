from django.http import JsonResponse
from .services import get_activity_count_by_type


def activity_summary(request):
    data = list(get_activity_count_by_type())
    return JsonResponse(data, safe=False)
