from django.urls import path
from .views import ActivePollList, AnswerList, AnswerDetail, MyAnswers
from .views import PollList, PollDetail, QuestionList, QuestionDetail

urlpatterns = [
    path('activepolls/<int:pk>/', PollDetail.as_view()),
    path('activepolls/', ActivePollList.as_view()),
    path('polls/<int:pk>/', PollDetail.as_view()),
    path('polls/', PollList.as_view()),
    path('questions/<int:pk>/', QuestionDetail.as_view()),
    path('questions/', QuestionList.as_view()),
    path('answers/<int:pk>/', AnswerDetail.as_view()),
    path('answers/', AnswerList.as_view()),
    path('myanswers/', MyAnswers.as_view()),
]
