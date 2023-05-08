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


class RegisterTest(models.Model):
    question_name = models.TextField()

    def __str__(self):
        return self.question_name


class RegisterTestVariant(models.Model):
    name = models.TextField()
    test = models.ForeignKey(RegisterTest, on_delete=models.CASCADE, related_name='first_variant')

    def __str__(self):
        return self.name


class RegisterVariantsVariant(models.Model):
    name = models.TextField()
    var = models.ForeignKey(RegisterTestVariant, on_delete=models.CASCADE, related_name='second_variant')

    def __str__(self):
        return self.name


class ThirdVariant(models.Model):
    name = models.TextField()
    var = models.ForeignKey(RegisterVariantsVariant, on_delete=models.CASCADE, related_name='third_variant')

    def __str__(self):
        return self.name


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
