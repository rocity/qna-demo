from django.urls import path

from .views import QuestionsTemplateView


urlpatterns = [
    path('questions/', QuestionsTemplateView.as_view(), name='questions')
]
