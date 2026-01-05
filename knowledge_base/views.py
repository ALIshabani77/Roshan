from django.shortcuts import render
from .models import Document, QuestionResponse
from django.db.models import Q

def ask_ai(request):
    query = request.GET.get('q')
    context = {}

    if query:
        
        question_obj = QuestionResponse.objects.create(question_text=query)

        results = Document.objects.filter(
            Q(title__icontains=query) |  
            Q(content__icontains=query) | 
            Q(tags__icontains=query)
        ).distinct()

        if results.exists():
            question_obj.related_documents.add(*results)

            question_obj.answer_text = f"بر اساس اسناد یافت شده: {results.first().content[:200]}..."
        else:
            question_obj.answer_text = "متأسفانه سندی مرتبط با سوال شما پیدا نشد."
        
        question_obj.save()
        
        context['question'] = question_obj
        context['results'] = results

    return render(request, 'knowledge_base/ask.html', context)


def document_detail(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'knowledge_base/document_detail.html', {'document': document})