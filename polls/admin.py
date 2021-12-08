from django.contrib import admin

from .models import Choice, Poll, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll', 'text', 'choice_type']})
    ]
    inlines = [ChoiceInLine]


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'started_at', 'finished_at', 'description']})
    ]
    inlines = [QuestionInLine]
    list_display = ('name', 'description', 'is_active')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Poll, PollAdmin)
