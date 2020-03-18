from django.urls import path
from .views import HomePageView, SamplePageView, FuncionaPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('funciona/', FuncionaPageView.as_view(), name="funciona"),
]