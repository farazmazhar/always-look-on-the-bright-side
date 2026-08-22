"""URL routing — mix of explicit paths and a router-generated set.

A DefaultRouter automatically builds the URL table for a ViewSet:
    /books/        GET    -> list   POST   -> create
    /books/<id>/   GET    -> detail PUT    -> update
                   PATCH  -> partial update  DELETE -> destroy
It also serves the browsable API at /api/ (drf's own UI).
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("books", views.BookViewSet, basename="book")

urlpatterns = [
    # function-based endpoints
    path("books/", views.book_list),
    path("books/<int:pk>/", views.book_detail),
    # class-based endpoint (same paths, different handler)
    path("api/books/", views.BookListAPIView.as_view()),
    # router-generated CRUD under /api/
    path("api/", include(router.urls)),
]
