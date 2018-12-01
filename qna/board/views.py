from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from board.models import Question
from board.forms import QuestionForm


class QuestionsTemplateView(TemplateView):
    """
    Renders questions as a list
    """

    template_name = 'board/questions.html'

    def get_context_data(self, *args, **kwargs):
        data = super(QuestionsTemplateView, self).get_context_data(*args, **kwargs)

        data['questions'] = Question.objects.all()
        data['form'] = QuestionForm()
        return data


class QuestionDetailView(DetailView):
    """
    Question details
    """

    model = Question


class QuestionCreateView(TemplateView):
    """
    View to ask questions
    """

    template_name = 'board/question_create.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        context.update({
            'form': QuestionForm(),
        })

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        context.update({
            'form': QuestionForm(),
        })

        post_data = request.POST.copy()
        data = {
            'user': request.user,
            'title': post_data.get('title'),
            'body': post_data.get('body')
        }

        form = QuestionForm(data)

        if form.is_valid():
            question = Question.objects.create(**form.data)
            context.update({
                'success': True,
                'question': question
            })
            return render(request, self.template_name, context)

        # Fall here by default if not valid
        context.update({
            'form': form
        })

        return render(request, self.template_name, context)

