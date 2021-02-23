from django_filters import FilterSet, CharFilter

from .models import *

class SequenceFilter(FilterSet):
    effector_id = CharFilter(field_name="effector_id", lookup_expr="icontains")
    effector_name = CharFilter(field_name="effector_name", lookup_expr="icontains")
    effector_signal_peptide = CharFilter(field_name="effector_sequence", lookup_expr="icontains")

    class Meta:
        model = Sequence
        fields = "__all__"
