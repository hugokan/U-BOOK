from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Event
from .forms import EventForm

class StaffRequiredMixin(object):
    """
    Este mixin requerira que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class EventListView(ListView):
    model = Event
    paginate_by = 4

class EventDetailView(DetailView):
    model = Event

@method_decorator(staff_member_required, name='dispatch')   
class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('events:events')
    
@method_decorator(staff_member_required, name='dispatch')   
class EventUpdate(UpdateView):
    model = Event
    form_class = EventForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('events:update', args=[self.object.id]) + '?ok'
    
@method_decorator(staff_member_required, name='dispatch')   
class EventDelete(DeleteView):
    model = Event
    success_url = reverse_lazy('events:events')