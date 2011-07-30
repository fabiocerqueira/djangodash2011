import datetime
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from activity.models import Event, Presentation

admin.autodiscover()

from django.views.generic.base import TemplateView


class HomepageTeplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageTeplateView, self).get_context_data(**kwargs)

        events = Event.objects.order_by('-event_start')
        context['events'] = events
        
        presentations = Presentation.objects.filter(event=Event.objects.latest('event_start'))
        context['presentations'] = presentations

        return context


urlpatterns = patterns('',
    url(r'^activity/', include('activity.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('registration.urls')),
    url(r'^$', HomepageTeplateView.as_view(), name='homepage'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
