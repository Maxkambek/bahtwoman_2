from rest_framework import serializers
from .models import Question, QuestionVariant, UserQuestion, MainTest, RegisterTest


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


class QuestionDetailSerializer(serializers.ModelSerializer):
    question_variants = QuestionVariantSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'image', 'price', 'text_desc', 'question', 'some_title', 'red_title', 'question_variants',
                  'comment']


class MainTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTest
        fields = ['id', 'question', 'answer_a', 'answer_b', 'answer_c', 'answer_d','answer_e']


class UserQuestionSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer()

    class Meta:
        model = UserQuestion
        fields = ['question', 'is_paid']
