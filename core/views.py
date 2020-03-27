from django.views.generic.base import TemplateView
from django.shortcuts import render
from libros.models import Libro
from django.views.generic.list import ListView

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    class LibroListView(ListView):
        model = Libro
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"E-BOOK"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
    
class FuncionaPageView(TemplateView):
    template_name = "core/funciona.html"