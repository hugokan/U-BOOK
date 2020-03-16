from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Libro
from .forms import LibroForm

class LoginRequired(object):
    """
    Este mixin requerirá que el usuario sea miembro registrado
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequired, self).dispatch(request, *args, **kwargs)

# Create your views here.
class LibroListView(ListView):
    model = Libro

class LibroDetailView(DetailView):
    model = Libro

@method_decorator(login_required, name='dispatch')
class LibroCreate(CreateView):
    model = Libro
    form_class = LibroForm
    success_url = reverse_lazy('libros:libros')

@method_decorator(login_required, name='dispatch')
class LibroUpdate(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('libros:update', args=[self.object.id]) + '?ok'

@method_decorator(login_required, name='dispatch')
class LibroDelete(DeleteView):
    model = Libro
    success_url = reverse_lazy('libros:libros')