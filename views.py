from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Sequence
from .filters import SequenceFilter

def index(request):
    return render(request, "database/index.html")

def submit(request):
    return render(request, "database/submit.html")

def submitted(request):
    try:
        new_seq = Sequence(
            effector_id=request.POST.get("effector_id"),
            effector_sequence=request.POST.get("effector_sequence")
        )

        if not new_seq.effector_id or not new_seq.effector_sequence:
            raise ValueError

    except ValueError:
        return render(request, "database/submit.html", {
            "error_message": "Please fill in all the forms"
        })
    # Add a confirmation page
    new_seq.save()
    return HttpResponseRedirect(reverse("database:index"))

def databaseViewer(request):
    effector_sequences = Sequence.objects.all()
    search_filter = SequenceFilter(request.GET, queryset=effector_sequences)
    effector_sequences = search_filter.qs

    context = {"effector_sequences": effector_sequences, "search_filter": search_filter}
    return render(request, "database/databaseViewer.html", context)
