from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response 

from words.models import Words
from .game_logic import get_game_question
from .serializers import WordsSerializer


class WordsPagination(PageNumberPagination):
    page_size = 10

class WordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    pagination_class = WordsPagination
    
    @action(detail=False, methods=['get'], url_path='game')
    def game(self, request):
        result = get_game_question(self.get_queryset())
        return Response(result)

