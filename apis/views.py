from rest_framework import generics
from books.models import Books
from .serializers import BookSerializer
# Create your views here.

class BookApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
