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
    error_message = ""
    try:
        post_effector_id = request.POST.get("effector_id", "")
        post_effector_sequence = request.POST.get("effector_sequence", "")
        post_effector_name = request.POST.get("effector_name", "")
        post_effector_description = request.POST.get("effector_description", "")
        post_effector_signal_peptide = request.POST.get("effector_signal_peptide", False)

        print(post_effector_signal_peptide)
        print(type(post_effector_signal_peptide))
        if Sequence.objects.filter(effector_id=post_effector_id).count() != 0:
            error_message = "'{}' already exists".format(post_effector_id)
            raise ValueError

        new_seq = Sequence(
            effector_id=post_effector_id,
            effector_sequence=post_effector_sequence,
            effector_name=post_effector_name,
            effector_description=post_effector_description,
            # effector_signal_peptide=post_effector_signal_peptide
        )

        if not new_seq.effector_id:
            error_message = "Please fill in the 'effector ID' field"
            raise ValueError
        elif not new_seq.effector_sequence:
            error_message = "Please fill in the 'DNA sequence' field"
            raise ValueError


    except ValueError:
        return render(request, "database/submit.html", {
            "error_message": error_message,
            "post_effector_id": post_effector_id,
            "post_effector_sequence": post_effector_sequence
        })
    # Add a confirmation page
    new_seq.save()
    return HttpResponseRedirect(reverse("database:databaseViewer"))

def databaseViewer(request):
    effector_sequences = Sequence.objects.all()
    search_filter = SequenceFilter(request.POST, queryset=effector_sequences)
    effector_sequences = search_filter.qs

    search_effector_id = request.POST.get("effector_id", "")
    search_effector_sequence = request.POST.get("effector_sequence", "")

    context = {
        "effector_sequences": effector_sequences,
        "search_effector_id": search_effector_id,
        "search_effector_sequence": search_effector_sequence
    }
    return render(request, "database/databaseViewer.html", context)

def deleteSequence(request):
    error_message = ""
    try:
        effector_id = request.POST.get("effector_id", "")
        if Sequence.objects.filter(effector_id=effector_id).count() == 0:
            error_message = "'{}' does not exists".format(effector_id)
            raise ValueError

        Sequence.objects.get(effector_id=effector_id).delete()

    except ValueError:
        return HttpResponseRedirect(reverse("database:databaseViewer"))

    return HttpResponseRedirect(reverse("database:databaseViewer"))
























