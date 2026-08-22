"""Views — DRF builds on Django's request/response cycle and makes it
JSON-native. Three levels of abstraction, from explicit to declarative:

  @api_view        -> function views with Request/Response objects
  APIView          -> class-based, method = HTTP verb
  ViewSet + router -> whole CRUD API from a model in a few lines
"""

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookModelSerializer, BookSerializer


# ---------------------------------------------------------------------------
# 1. @api_view — the smallest step up from a plain Django view.
#    DRF's Request parses the JSON body; DRF's Response renders JSON.
# ---------------------------------------------------------------------------
@api_view(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        # .data is already JSON-ready: no manual dict building.
        return Response(BookSerializer(books, many=True).data)

    # POST: validate the body against the serializer, like pydantic.
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def book_detail(request, pk: int):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    return Response(BookSerializer(book).data)


# ---------------------------------------------------------------------------
# 2. APIView — the same thing as a class: each HTTP verb is a method.
#    Django's class-based views, but with Request/Response/status codes.
# ---------------------------------------------------------------------------
class BookListAPIView(APIView):
    def get(self, request):
        return Response(BookModelSerializer(Book.objects.all(), many=True).data)

    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------------------------------------------------------------------------
# 3. ModelViewSet + router — the full CRUD API with zero handler code.
#    GET /books/ (list), POST /books/ (create), GET/PUT/PATCH/DELETE
#    /books/<id>/ — all generated from the serializer + model.
# ---------------------------------------------------------------------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
