from django.urls import path
from .views import BookListView, BookDetailView, BookCreate, BookUpdate, BookDelete

books_patterns = ([
    path('', BookListView.as_view(), name='books'),
    path('<int:pk>/<slug:slug>/', BookDetailView.as_view(), name='book'),
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete'),
], 'books')