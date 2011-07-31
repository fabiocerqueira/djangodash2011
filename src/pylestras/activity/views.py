# -*- coding:utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from activity.models import Event, Presentation
from activity.forms import EventCreateForm, PresentationFormSet


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
        context = self.get_context_data()
        self.object = form.save(commit=False)
        self.object.admin = self.request.user
        presentation_formset = context['presentation_formset']
        if presentation_formset.is_valid():
            self.object.save()
            presentation_formset.instance = self.object
            presentation_formset.save()
            messages.success(self.request, _('Event %s registered successfully!') % self.object.name)
            return super(DashboardCreateEvent, self).form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(DashboardCreateEvent, self).get_context_data(**kwargs)
        if self.request.POST:
            context['presentation_formset'] = PresentationFormSet(self.request.POST)
        else:
            context['presentation_formset'] = PresentationFormSet()
        return context
