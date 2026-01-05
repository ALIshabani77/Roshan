from django.urls import path
from .views import ask_ai,document_detail


app_name = 'knowledge_base'

urlpatterns = [
    path('ask/', ask_ai, name='ask_ai'),
    path('document/<int:pk>/', document_detail, name='document_detail'),
]