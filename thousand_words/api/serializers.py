from rest_framework import serializers

from words.models import Words


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ('word', 'translation')


class GameQuerySerializer(serializers.Serializer):
    count = serializers.IntegerField(
        min_value=1,
        max_value=100,
        required=False,
        default=1,
        help_text="Questions count"
    )