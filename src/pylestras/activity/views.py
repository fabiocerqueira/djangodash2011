from django.views.generic import ListView

from activity.models import Event


class DashboardListView(ListView):
    context_object_name = "event_list"
    template_name='activity/dashboard/index.html'

    def get_queryset(self):
        return Event.objects.filter(admin=self.request.user)
