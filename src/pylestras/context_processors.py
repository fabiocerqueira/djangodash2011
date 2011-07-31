# -*- coding: utf-8 -*-
from activity.models import Event

def site_context_processors(request):
    events = Event.objects.order_by('-event_start')[:10]
    return {
        'events': events,
    }
