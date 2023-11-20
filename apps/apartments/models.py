from datetime import datetime

from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('cancel', 'Отмена'),
        ('purchase', 'Куплено'),
        ('reserve', 'Бронь'),
        ('barter', 'Бартер'),
        ('installment', 'Рассроч'),
        ('active', 'Активный'),
    ]
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    floor = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.CharField(max_length=255)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    kv = models.DecimalField(max_digits=10, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}"
