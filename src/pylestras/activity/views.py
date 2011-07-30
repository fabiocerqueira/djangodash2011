# -*- coding:utf-8 -*-
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from activity.models import Event, Presentation


class EventDetailView(DetailView):
    model = Event
    context_object_name = "event"

class PresentationDetailView(DetailView):
    model = Presentation
    context_object_name = 'presentation'

class DashboardListView(ListView):
    context_object_name = "event_list"
    template_name='activity/dashboard/index.html'

    def get_queryset(self):
        return Event.objects.filter(admin=self.request.user)


#class DashboardAddEvent(
