from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .constants import CHOICE_TYPES


class Poll(models.Model):
    name = models.CharField(max_length=50) # need Uniq
    started_at = models.DateTimeField('date started')
    finished_at = models.DateTimeField('date finished')
    description = models.CharField(max_length=200)

    def is_active(self):
        if timezone.now() > self.started_at and timezone.now() < self.finished_at:
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, null=True, on_delete=models.CASCADE)
    choice_type = models.CharField(
        max_length=11,
        choices=CHOICE_TYPES
    )
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=True, null=True)
    # user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(default=timezone.now(), editable=False)

    def __str__(self):
        return self.text
