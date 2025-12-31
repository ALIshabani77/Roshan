from django.contrib import admin
from .models import Document, QuestionResponse

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_summary', 'created_at')
    search_fields = ('title', 'content', 'tags')
    list_filter = ('created_at',)

    def get_summary(self, obj):
        return obj.content[:100] + "..."
    get_summary.short_description = "خلاصه متن"

@admin.register(QuestionResponse)
class QuestionResponseAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'created_at')