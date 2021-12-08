from django.db.models import Prefetch
from django.utils import timezone
from rest_framework import generics, permissions
from .models import Poll, Question
from .serializers import PollSerializer, QuestionSerializer


class ActivePollList(generics.ListCreateAPIView):
    serializer_class = PollSerializer

    def get_queryset(self):
        today = timezone.now()
        queryset = Poll.objects.filter(
            started_at__lt=today,
            finished_at__gt=today
        )
        return queryset


class PollList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
