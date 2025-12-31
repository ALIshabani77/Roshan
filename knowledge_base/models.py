from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان")
    content = models.TextField(verbose_name="متن کامل")
    tags = models.CharField(max_length=255, verbose_name="برچسب‌ها (با کاما جدا کنید)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.title

class QuestionResponse(models.Model):
    question_text = models.TextField(verbose_name="پرسش کاربر")
    answer_text = models.TextField(null=True, blank=True, verbose_name="پاسخ سیستم")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text[:50]