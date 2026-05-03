from rest_framework import viewsets

from words.models import Words
from .serializers import WordsSerializer


class WordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer