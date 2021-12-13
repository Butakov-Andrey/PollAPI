from django.utils import timezone
from rest_framework import filters, generics, permissions
from .models import Answer, Poll, Question
from .permissions import ReadOnly
from .serializers import AnswerSerializer, PollSerializer
from .serializers import QuestionSerializer, MyAnswersSerializer


class ActivePollList(generics.ListCreateAPIView):
    permission_classes = [ReadOnly]
    serializer_class = PollSerializer

    def get_queryset(self):
        today = timezone.now()
        queryset = Poll.objects.filter(
            started_at__lt=today,
            finished_at__gt=today
        )
        return queryset


class PollList(generics.ListCreateAPIView):
    serializer_class = PollSerializer
    queryset = Poll.objects.all()


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class QuestionList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class MyAnswers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Answer.objects.all()
    serializer_class = MyAnswersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user']
