from django.urls import path
from .views import ActivePollList, PollList, PollDetail, QuestionList, QuestionDetail

urlpatterns = [
    path('polls/<int:pk>/', PollDetail.as_view()),
    path('polls/', ActivePollList.as_view()),
    path('allpolls/', PollList.as_view()),
    path('questions/<int:pk>/', QuestionDetail.as_view()),
    path('questions/', QuestionList.as_view()),
]
