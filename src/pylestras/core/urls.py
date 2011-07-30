from django.conf.urls.defaults import patterns, url
from core.views import HomepageTeplateView

urlpatterns = patterns('',
    url(r'^$', HomepageTeplateView.as_view(), name='homepage'),
)
