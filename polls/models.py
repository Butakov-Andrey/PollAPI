from django.db import models
from django.utils import timezone
from .constants import CHOICE_TYPES


class Poll(models.Model):
    name = models.CharField(max_length=50)
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
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_type = models.CharField(
        max_length=11,
        choices=CHOICE_TYPES,
        default='TEXT'
    )
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
