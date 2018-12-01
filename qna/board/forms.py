from django import forms


class QuestionForm(forms.Form):
    """
    Form for creating Questions
    """

    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

    def is_valid(self):
        if self.data.get('body') == self.data.get('title'):
            self.errors.update({
                'duplicate': 'Your field values must not be the same'
            })
        return super(QuestionForm, self).is_valid()
