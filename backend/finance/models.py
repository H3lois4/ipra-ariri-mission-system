from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Expense(models.Model):
    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    receipt = models.FileField(upload_to='finance/receipts/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number} - {self.title}'
