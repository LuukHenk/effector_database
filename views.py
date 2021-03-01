from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Sequence
from .forms import SequenceForm

def index(request):
    return HttpResponseRedirect(reverse("database:search"))

def submit(request):
    form = SequenceForm()
    return render(request, "database/submit.html", {"form": form})

def submitted(request):
    if request.method == "POST":
        form = SequenceForm(request.POST)

        if form.is_valid():
            form.save()
            message = "Succesfully added '{}'".format(form.cleaned_data['effector_id'])
            messages.success(request, message)
            return HttpResponseRedirect(reverse("database:search"))

    else:
        form = SequenceForm()

    return render(request, "database/submit.html", {"form": form})

def search(request):
    context = {
        "effector_id": request.GET.get("effector_id", ""),
        "effector_name": request.GET.get("effector_name", ""),
        "effector_signal_peptide": request.GET.get("effector_signal_peptide", "")
    }

    context["query_set"] = Sequence.objects.filter(
        effector_id__icontains=context["effector_id"],
        effector_name__icontains=context["effector_name"],
        effector_signal_peptide__icontains=context["effector_signal_peptide"]
    )
    return render(request, "database/search.html", context)

def itemViewer(request, item_name):
    context = {
        "item": get_object_or_404(Sequence, pk=item_name)
    }
    return render(request, "database/itemViewer.html", context)


def deleteSequence(request, item_name):
    try:
        item = Sequence.objects.get(effector_id=item_name)
        Sequence.objects.get(effector_id=item_name).delete()
        message = "Succesfully deleted sequence with effector ID '{}'".format(item_name)
        messages.success(request, message)

    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(item_name)
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("database:search"))

    return HttpResponseRedirect(reverse("database:search"))
