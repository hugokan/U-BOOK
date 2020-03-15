from django.urls import path
from .views import EventListView, EventDetailView, EventCreate, EventUpdate, EventDelete

events_patterns = ([
    path('', EventListView.as_view(), name='events'),
    path('<int:pk>/<slug:slug>/', EventDetailView.as_view(), name='event'),
    path('create/', EventCreate.as_view(), name='create'),
    path('update/<int:pk>/', EventUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', EventDelete.as_view(), name='delete'),
], 'events')