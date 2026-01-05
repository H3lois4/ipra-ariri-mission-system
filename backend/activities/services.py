from django.db.models import Count
from .models import ActivityType


def get_activity_count_by_type():
    """
    Retorna uma lista com:
    [
        {'type': 'Evangelismo', 'count': 10},
        {'type': 'Visitação', 'count': 5},
        ...
    ]
    """
    return (
        ActivityType.objects
        .annotate(total=Count('activities'))
        .values('name', 'total')
        .order_by('name')
    )
