from django.contrib import admin
from .models import Question, Option, Language
# Register your models here.

class OptionInline(admin.TabularInline):
    model = Option
    extra = 0
    fk_name = "related_question"

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Option)
admin.site.register(Language)
admin.site.register(Question, QuestionAdmin)