from modeltranslation.translator import register, TranslationOptions
from .models import QuestionVariant, MainTest, \
    Question, Workout, QuestionVariantForFirst
from accounts.models import Region, District


@register(QuestionVariantForFirst)
class First(TranslationOptions):
    fields = ('text',)


@register(Region)
class RegionTrans(TranslationOptions):
    fields = ('name',)


@register(District)
class DistrictTrans(TranslationOptions):
    fields = ('name',)


@register(Workout)
class WorkoutTrans(TranslationOptions):
    fields = ('text',)


@register(MainTest)
class MainTestTrans(TranslationOptions):
    fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'answer_e')


@register(QuestionVariant)
class QuestionVariantTrans(TranslationOptions):
    fields = ('text',)


@register(Question)
class QuestionTrans(TranslationOptions):
    fields = ('text_desc', 'question', 'some_title', 'red_title', 'comment')
