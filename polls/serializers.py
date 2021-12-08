from django.utils import timezone
from rest_framework import serializers
from .models import Poll, Question


class PollSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField()

    def is_active(self, obj):
        if timezone.now() > self.started_at and timezone.now() < self.finished_at:
            return True
        else:
            return False

    class Meta:
        model = Poll
        fields = ('id', 'name', 'started_at', 'finished_at', 'description', 'is_active',)


class QuestionSerializer(serializers.ModelSerializer):
    poll_name = serializers.CharField(source='poll.name')

    class Meta:
        model = Question
        fields = ('poll_name', 'text', 'choice_type',)
