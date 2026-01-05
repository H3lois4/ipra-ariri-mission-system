from django.db import models


class Devotional(models.Model):
    title = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='devotionals/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
