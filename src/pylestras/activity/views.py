# -*- coding:utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib import messages

from activity.models import Event, Presentation
from activity.forms import EventCreateForm


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

class DashboardCreateEvent(CreateView):
    form_class = EventCreateForm
    model = Event
    template_name='activity/dashboard/event_add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.admin = self.request.user
        self.object.save()
        messages.success(self.request, 'Event %s registered successfully!' % self.object.name)
        return super(DashboardCreateEvent, self).form_valid(form)
        
