"""A minimal Django app so the demo can use real models + migrations.

In a real project this package would be created by `manage.py startapp`,
but a demo needs no more than models.py — Django discovers the rest.
"""

from django.db import models


class Article(models.Model):
    """One row in a 'demo_app_article' table — Django derives table names."""

    title = models.CharField(max_length=100)
    body = models.TextField()
    published = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
