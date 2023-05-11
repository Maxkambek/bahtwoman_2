from django.contrib import admin
from .models import Question, QuestionVariant, MainTest, RegisterTest, UserQuestion, Workout, QuestionVariantForFirst
from modeltranslation import admin as a

admin.site.register(UserQuestion)


class FirstAdmin(a.TranslationStackedInline):
    model = QuestionVariantForFirst
    extra = 1


class VarAdmin(a.TranslationStackedInline):
    model = QuestionVariant
    extra = 1


class WorkAdmin(a.TranslationStackedInline):
    model = Workout
    extra = 1


@admin.register(Question)
class QuestionAdmin(a.TranslationAdmin):
    inlines = [VarAdmin, WorkAdmin, FirstAdmin]


@admin.register(MainTest)
class TestAdmin(a.TranslationAdmin):
    pass
