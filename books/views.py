from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm

class LoginRequired(object):
    """
    Este mixin requerirá que el usuario sea miembro registrado
    """
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequired, self).dispatch(request, *args, **kwargs)

# Create your views here.
class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

@method_decorator(login_required, name='dispatch')
class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('books:books')

@method_decorator(login_required, name='dispatch')
class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('books:update', args=[self.object.id]) + '?ok'

@method_decorator(login_required, name='dispatch')
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:books')