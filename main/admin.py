from django.contrib import admin
from .models import Question, QuestionVariant, MainTest, RegisterTest, UserQuestion

admin.site.register(UserQuestion)


class VarAdmin(admin.StackedInline):
    model = QuestionVariant
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [VarAdmin]


admin.site.register(MainTest)
admin.site.register(RegisterTest)
