from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Choice, Question


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("La Questan", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInLine]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

AdminSite.site_header = "Polls Administration"

