from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required

from activity.views import * 

urlpatterns = patterns('',
    url(r'^event/(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name="activity_event"),
)

#dashboard urls
urlpatterns += patterns('',
    url(r'^dashboard/$', login_required(DashboardListView.as_view()), name="dashboard_index"),
)
