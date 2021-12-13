from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Answer, Poll, Question


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'text', 'choice_type', 'poll',)

    def create(self, validated_data):
        question = Question.objects.create(**validated_data)
        return question

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.choice_type = validated_data.get('choice_type', instance.choice_type)
        instance.save()
        return instance


class PollSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField('is_active')

    def is_active(self, obj):
        if timezone.now() > self.started_at and timezone.now() < self.finished_at:
            return True
        else:
            return False

    def validate_started_at(self, value):
        if self.context['request'].method == 'PUT':
            if value != self.instance.started_at:
                raise serializers.ValidationError("You can't edit this field.")
        return value

    class Meta:
        model = Poll
        fields = ('id', 'name', 'started_at', 'finished_at', 'description', 'is_active', 'question_set')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'text', 'user', 'date', )

    def create(self, validated_data):
        # Определение пользователя
        user = self.context['request'].user.pk
        user_field = self.context['request'].POST.get('user')
        # Если поле User пустое - вставляется значение определенного пользователя
        # Если пользователь не определен - вставляется значение token из cookies
        if user_field == '':
            if get_user_model().objects.filter(pk=user):
                removed_data = validated_data.pop('user')
                answer = Answer.objects.create(user=user, **validated_data)
                return answer
            else:
                user = self.context['request'].META.get('CSRF_COOKIE')
                removed_data = validated_data.pop('user')
                answer = Answer.objects.create(user=user, **validated_data)
                return answer
        answer = Answer.objects.create(**validated_data)
        return answer

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.text = validated_data.get('text', instance.text)
        instance.user = validated_data.get('user', instance.user)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class MyAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'text', 'user', 'date',)
        read_only_fields = ('question', 'text', 'user',)
