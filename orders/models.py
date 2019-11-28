from django.db import models
from decimal import Decimal


class Orders(models.Model):
    size = models.CharField(max_length=1)
    crust = models.CharField(max_length=5)
    toppings = models.CharField(max_length=20)
    cost = models.DecimalField(
        max_digits=20, decimal_places=2, default=Decimal('0.00'))
    location = models.CharField(max_length=50)
