# Create your views here.
from django.views.generic.base import TemplateView

class HomepageTeplateView(TemplateView):
    template_name = 'index.html'
