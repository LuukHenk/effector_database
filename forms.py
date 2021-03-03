from django.forms import ModelForm
from .models import Sequence

class SequenceForm(ModelForm):
    """ Generates a form for the sequence database """
    class Meta:
        model = Sequence
        fields = "__all__"
