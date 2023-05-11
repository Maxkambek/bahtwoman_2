from rest_framework import serializers
from .models import Question, QuestionVariant, UserQuestion, MainTest, RegisterTest, Workout, QuestionVariantForFirst


class ForFirst(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariantForFirst
        fields = ['id', 'text']


class RegisterTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterTest
        fields = ['question_name', 'answer']


class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = ['id', 'text']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question']


class WorkOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'text']


class QuestionDetailSerializer(serializers.ModelSerializer):
    question_variants = QuestionVariantSerializer(many=True)
    work_outs = WorkOutSerializer(many=True)
    for_first_question = ForFirst(many=True)

    class Meta:
        model = Question
        fields = ['id', 'image', 'price', 'text_desc', 'question', 'some_title', 'red_title', 'for_first_question',
                  'question_variants',
                  'comment', 'work_outs']


class MainTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTest
        fields = ['id', 'question', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'answer_e']


class UserQuestionSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer()

    class Meta:
        model = UserQuestion
        fields = ['question', 'is_paid']
