from modeltranslation.translator import register, TranslationOptions
from .models import RegisterTestVariant, RegisterTest, RegisterVariantsVariant, ThirdVariant, QuestionVariant, MainTest, \
    Question


@register(MainTest)
class MainTestTrans(TranslationOptions):
    fields = ('question', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'true_answer')


@register(RegisterTest)
class RegisterTrans(TranslationOptions):
    fields = ('question_name',)


@register(RegisterTestVariant)
class RegisterTestTrans(TranslationOptions):
    fields = ('name',)


@register(RegisterVariantsVariant)
class RegisterSecTrans(TranslationOptions):
    fields = ('name',)


@register(ThirdVariant)
class RegisterThirdTrans(TranslationOptions):
    fields = ('name',)


@register(QuestionVariant)
class QuestionVariantTrans(TranslationOptions):
    fields = ('text',)


@register(Question)
class QuestionTrans(TranslationOptions):
    fields = ('text_desc', 'question', 'some_title', 'red_title', 'comment')
