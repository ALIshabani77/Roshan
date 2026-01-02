from django.contrib import admin
from .models import Document, QuestionResponse

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_summary', 'created_at')
    search_fields = ('title', 'content', 'tags')
    list_filter = ('created_at',)

    def get_summary(self, obj):
        return obj.content[:100] + "..." if obj.content else ""
    get_summary.short_description = "خلاصه متن"

@admin.register(QuestionResponse)
class QuestionResponseAdmin(admin.ModelAdmin):
    
    list_display = ('get_question_summary', 'get_answer_summary', 'created_at')
    
    list_filter = ('created_at',)
    
    search_fields = ('question_text', 'answer_text')
    
    filter_horizontal = ('related_documents',)

    def get_question_summary(self, obj):
        return obj.question_text[:50] + "..."
    get_question_summary.short_description = "پرسش"

    def get_answer_summary(self, obj):
        if obj.answer_text:
            return obj.answer_text[:50] + "..."
        return "هنوز پاسخی ثبت نشده"
    get_answer_summary.short_description = "پاسخ سیستم"