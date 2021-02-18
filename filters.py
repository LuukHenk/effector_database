from django_filters import FilterSet, CharFilter

from .models import *

class SequenceFilter(FilterSet):
    effector_id = CharFilter(field_name="effector_id", lookup_expr="icontains")
    effector_sequence = CharFilter(field_name="effector_id", lookup_expr="icontains")
    class Meta:
        model = Sequence
        fields = "__all__"
