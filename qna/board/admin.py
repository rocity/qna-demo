from django.contrib import admin

from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''
    Admin View for Question
    '''
    list_display = ('user', 'title', 'body',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    '''
    Admin View for Answer
    '''
    list_display = ('question', 'user', 'body',)
