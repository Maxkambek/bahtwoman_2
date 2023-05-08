from django.contrib import admin
from .models import Question, QuestionVariant, MainTest, RegisterTest, UserQuestion, RegisterTestVariant, \
    RegisterVariantsVariant, ThirdVariant

admin.site.register(UserQuestion)
admin.site.register(RegisterTestVariant)
admin.site.register(RegisterVariantsVariant)
admin.site.register(ThirdVariant)


class VarAdmin(admin.StackedInline):
    model = QuestionVariant
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [VarAdmin]


admin.site.register(MainTest)
admin.site.register(RegisterTest)
