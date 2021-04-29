from django.urls import path, re_path
from book import views

urlpatterns = [
    re_path('add_book$', views.add_book),
    re_path('show_books/', views.show_books),
    re_path('delete_book/', views.delete_book),
]