from django import forms


class QuestionForm(forms.Form):
    """
    Form for creating Questions
    """

    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
