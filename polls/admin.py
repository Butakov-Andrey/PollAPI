from django.contrib import admin

from .models import Answer, Poll, Question


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


class AnswerInLine(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll', 'text', 'choice_type']})
    ]
    inlines = [AnswerInLine]


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'started_at', 'finished_at', 'description']})
    ]
    inlines = [QuestionInLine]
    list_display = ('name', 'description', 'is_active')


class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question', 'text', 'user']})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll, PollAdmin)
admin.site.register(Answer, AnswerAdmin)
