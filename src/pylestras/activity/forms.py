from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from activity.models import Event, Presentation

class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        exclude = ('admin', 'slug') 


PresentationFormSet = inlineformset_factory(Event,
    Presentation,
    can_delete=False,
    extra=3)
