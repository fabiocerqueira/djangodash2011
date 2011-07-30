from django.forms import ModelForm

from activity.models import Event

class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('admin', 'slug') 

