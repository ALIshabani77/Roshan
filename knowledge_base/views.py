from django.shortcuts import render
from .models import Document, QuestionResponse
from django.db.models import Q

def ask_ai(request):
    query = request.GET.get('q')
    context = {}

    if query:
        question_obj = QuestionResponse.objects.create(question_text=query)

        words = query.split()

        search_query = Q()
        for word in words:
            search_query |= Q(title__icontains=word) | Q(content__icontains=word) | Q(tags__icontains=word)

        results = Document.objects.filter(search_query).distinct()

        if results.exists():
            question_obj.related_documents.add(*results)
            question_obj.answer_text = f"بر اساس اسناد یافت شده: {results.first().content[:200]}..."
        else:
            question_obj.answer_text = "متأسفانه سندی مرتبط با سوال شما پیدا نشد."
        
        question_obj.save()
        context['question'] = question_obj
        context['results'] = results

    return render(request, 'knowledge_base/ask.html', context)