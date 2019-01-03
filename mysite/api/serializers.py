from polls.models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'pk')

    def create(self, validated_data):
        question = super(QuestionSerializer, self).create(validated_data)
        question.save()
        return question

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')