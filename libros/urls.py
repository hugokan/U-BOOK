from django.urls import path
from .views import LibroListView, LibroDetailView, LibroCreate, LibroUpdate, LibroDelete

libros_patterns = ([
    path('', LibroListView.as_view(), name='libros'),
    path('<int:pk>/<slug:slug>/', LibroDetailView.as_view(), name='libro'),
    path('create/', LibroCreate.as_view(), name='create'),
    path('update/<int:pk>/', LibroUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', LibroDelete.as_view(), name='delete'),
], 'libros')