from django.urls import path
from core import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('books/', views.book_list, name='all_books'),
    path('books/<int:id>/', views.book_detail, name='book_details'),
    path('readers/', views.reading_list, name='all_readers'),
    path('readers/<int:id>/', views.reading_details, name='reading_details'),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
