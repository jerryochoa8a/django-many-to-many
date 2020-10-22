from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.addbook),
    path('books/<book_id>/delete', views.book_delete),
    path('books/<book_id>', views.bookpage),
    path('books/<book_id>/add_author', views.bookauthor),

    path('author', views.author_index),
    path('addauthor', views.addauthor),
    path('author/<author_id>/delete', views.author_delete),
    path('author/<author_id>', views.authorpage),
    path('author/<author_id>/add_book', views.authorbook),
    
]