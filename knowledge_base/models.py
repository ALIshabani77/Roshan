from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان سند")
    content = models.TextField(verbose_name="متن کامل محتوا")
    tags = models.CharField(max_length=255, verbose_name="برچسب‌ها", help_text="با کاما جدا کنید")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "سند"
        verbose_name_plural = "اسناد"

class QuestionResponse(models.Model):
    question_text = models.TextField(verbose_name="پرسش کاربر")
    answer_text = models.TextField(null=True, blank=True, verbose_name="پاسخ سیستم")
    related_documents = models.ManyToManyField(Document, blank=True, verbose_name="اسناد مرتبط")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت")

    def __str__(self):
        return f"پرسش: {self.question_text[:30]}..."

    class Meta:
        verbose_name = "پرسش و پاسخ"
        verbose_name_plural = "پرسش‌ها و پاسخ‌ها"