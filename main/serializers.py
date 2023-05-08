from rest_framework import serializers
from .models import Question, QuestionVariant, UserQuestion, MainTest, RegisterTest, RegisterTestVariant, \
    RegisterVariantsVariant, ThirdVariant


class ThirdVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdVariant
        fields = ['name']


class VariantsVariantSerializer(serializers.ModelSerializer):
    third_variant = ThirdVariantSerializer(many=True)

    class Meta:
        model = RegisterVariantsVariant
        fields = ['name', 'third_variant']


class RegisterVariantSerializer(serializers.ModelSerializer):
    second_variant = VariantsVariantSerializer(many=True)

    class Meta:
        model = RegisterTestVariant
        fields = ['name', 'second_variant']


class RegisterTestSerializer(serializers.ModelSerializer):
    first_variant = RegisterVariantSerializer(many=True)

    class Meta:
        model = RegisterTest
        fields = ['id', 'question_name', 'first_variant']


class QuestionVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionVariant
        fields = ['id', 'text']


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'price', 'image']


class QuestionDetailSerializer(serializers.ModelSerializer):
    question_variants = QuestionVariantSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'image', 'price', 'text_desc', 'question', 'some_title', 'red_title', 'question_variants',
                  'comment']


class MainTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainTest
        fields = ['id', 'question', 'answer_a', 'answer_b', 'answer_c', 'answer_d']


class UserQuestionSerializer(serializers.ModelSerializer):
    question = QuestionListSerializer()

    class Meta:
        model = UserQuestion
        fields = ['question', 'is_paid']
