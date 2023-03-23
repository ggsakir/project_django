from django.db import models


class CreateModel(models.Model):
    """Добавляет дату создания"""
    created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )

    class Meta:
        abstract = True
