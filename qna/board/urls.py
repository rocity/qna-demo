from django.urls import path

from .views import QuestionsTemplateView, QuestionDetailView


urlpatterns = [
    path('questions/', QuestionsTemplateView.as_view(), name='questions'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question')
]
