from django.urls import path, re_path

from .views import (
    QuestionsTemplateView,
    QuestionDetailView,
    QuestionCreateView,
)

app_name = 'board'
urlpatterns = [
    path('questions/', QuestionsTemplateView.as_view(), name='questions'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question'),
    path('question/create/', QuestionCreateView.as_view(), name='question-create'),
]
