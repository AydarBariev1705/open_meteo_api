from django.db import models


class City(models.Model):
    """Модель города"""
    class Meta:
        ordering = '-views',
    name = models.CharField(
        max_length=200,
        db_index=True,
    )
    views = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.name!r}'
