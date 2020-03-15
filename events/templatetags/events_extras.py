from django import template
from events.models import Event

register = template.Library()

@register.simple_tag
def get_event_list():
    events = Event.objects.all()
    return events