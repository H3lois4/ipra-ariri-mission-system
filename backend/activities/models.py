from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ActivityType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    activity_type = models.ForeignKey(
        ActivityType,
        on_delete=models.PROTECT,
        related_name='activities'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='activities'
    )

    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='activities/photos/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.activity_type.name} - {self.created_at.strftime("%d/%m/%Y")}'
