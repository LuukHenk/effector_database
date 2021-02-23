from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Sequence
from .forms import SequenceForm

def index(request):
    return render(request, "database/index.html")

def submit(request):
    form = SequenceForm()
    return render(request, "database/submit.html", {"form": form})

def submitted(request):
    if request.method == "POST":
        form = SequenceForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("database:databaseViewer"))

    else:
        form = SequenceForm()

    return render(request, "database/submit.html", {"form": form})

def databaseViewer(request):
    context = {
        "error_message": "",
        "effector_id": request.GET.get("effector_id", ""),
        "effector_name": request.GET.get("effector_name", ""),
        "effector_signal_peptide": request.GET.get("effector_signal_peptide", "")
    }

    context["query_set"] = Sequence.objects.filter(
        effector_id__icontains=context["effector_id"],
        effector_name__icontains=context["effector_name"],
        effector_signal_peptide__icontains=context["effector_signal_peptide"]
    )
    return render(request, "database/databaseViewer.html", context)

def itemViewer(request, item_name):
    context = {
        "error_message": "",
        "item": get_object_or_404(Sequence, pk=item_name)
    }
    return render(request, "database/itemViewer.html", context)


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
