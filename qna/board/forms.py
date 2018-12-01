from django import forms

from board.models import Question


class QuestionModelForm(forms.ModelForm):
    """
    Question Model Form
    """

    class Meta:
        model = Question
        fields = ('user', 'title', 'body')
