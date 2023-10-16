from django.urls import path
from reading import views

urlpatterns = [
    path('', views.reading, name='reading'),
    path('statistics/', views.statistics, name='statistics'),
]