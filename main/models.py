from django.db import models
from accounts.models import User


class Question(models.Model):
    text_desc = models.TextField()
    question = models.TextField()
    some_title = models.TextField(null=True, blank=True)
    red_title = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}'


class QuestionVariant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_variants')
    text = models.TextField()


class RegisterTest(models.Model):
    question = models.TextField()

    def __str__(self):
        return f'{self.id}'


class MainTest(models.Model):
    question = models.TextField()
    answer_a = models.CharField(max_length=221)
    answer_b = models.CharField(max_length=221)
    answer_c = models.CharField(max_length=221, null=True, blank=True)
    answer_d = models.CharField(max_length=221, null=True, blank=True)
    true_answer = models.CharField(max_length=221)

    def __str__(self):
        return f'{self.id}'


class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='paid_questions')
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone
