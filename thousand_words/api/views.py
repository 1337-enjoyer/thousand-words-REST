from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from words.models import Words
from .game_logic import get_game_question, get_multiple_questions
from .serializers import GameQuerySerializer, WordsSerializer


class WordsPagination(PageNumberPagination):
    page_size = 10


class WordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    pagination_class = WordsPagination

    @swagger_auto_schema(
        method='get',
        query_serializer=GameQuerySerializer,
        responses={
            200: openapi.Response(
                description='Успешный ответ',
                examples={
                    'application/json': {
                        "word": "polite",
                        "translations": ["вежливый", "над", "вид"],
                        "solution": "вежливый"
                    }
                }
            )
        }
    )
    @action(detail=False, methods=['get'], url_path='game')
    def game(self, request):
        try:
            count = int(request.GET.get('count', 1))
            if count > 100:
                count = 100
            elif count < 1:
                count = 1
        except ValueError:
            count = 1

        if count == 1:
            result = get_game_question(self.get_queryset())
            return Response(result)

        result = get_multiple_questions(self.get_queryset(), count)
        return Response(result)
