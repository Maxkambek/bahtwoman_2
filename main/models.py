from django.db import models
from accounts.models import User


class Question(models.Model):
    text_desc = models.TextField()
    question = models.TextField()
    some_title = models.TextField(null=True, blank=True)
    red_title = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.id}'


class QuestionVariant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_variants')
    text = models.TextField()

    def __str__(self):
        return f'{self.id}'


class QuestionVariantForFirst(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='for_first_question')
    text = models.TextField()


class Workout(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='work_outs')

    def __str__(self):
        return f'{self.id}'


class RegisterTest(models.Model):
    question_name = models.TextField()
    answer = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_name


class MainTest(models.Model):
    question = models.TextField()
    answer_a = models.CharField(max_length=221)
    answer_b = models.CharField(max_length=221)
    answer_c = models.CharField(max_length=221, null=True, blank=True)
    answer_d = models.CharField(max_length=221, null=True, blank=True)
    answer_e = models.CharField(max_length=221, null=True, blank=True)
    true_answer = models.CharField(max_length=221)

    def __str__(self):
        return f'{self.id}'


class UserQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='paid_questions')
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone
