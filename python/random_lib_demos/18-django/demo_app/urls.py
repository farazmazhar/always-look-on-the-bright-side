"""URL configuration for the demo — in a real project this is the
project's urls.py. Referenced from settings via ROOT_URLCONF.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("articles/", views.article_list),
    # <int:> converts the URL segment to an int before the view sees it
    path("articles/<int:article_id>/", views.article_detail),
]
