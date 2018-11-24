from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from board.models import Question


class QuestionsTemplateView(TemplateView):
    """
    Renders questions as a list
    """

    template_name = 'board/questions.html'

    def get_context_data(self, *args, **kwargs):
        data = super(QuestionsTemplateView, self).get_context_data(*args, **kwargs)

        data['questions'] = Question.objects.all()
        return data


class QuestionDetailView(DetailView):
    """
    Question details
    """
    model = Question
