from django.urls import path
from core import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('books/', views.book_list, name='all_books'),
    path('books/<int:id>', views.book_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
