"""A minimal Django app so the DRF demo has a real model to serialize."""

from django.db import models


class Book(models.Model):
    """One row in a 'demo_app_book' table."""

    title = models.CharField(max_length=120)
    author = models.CharField(max_length=80)
    year = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
