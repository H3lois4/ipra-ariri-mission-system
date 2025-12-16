from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import TeamMember

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_team_member(sender, instance, created, **kwargs):
    if created:
        TeamMember.objects.create(
            user=instance,
            full_name=instance.name,
            email=instance.email,
            phone=''
        )
