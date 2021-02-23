from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Sequence

def index(request):
    return render(request, "database/index.html")

def submit(request):
    return render(request, "database/submit.html")

def submitted(request):
    try:
        context = {
            "effector_id": request.POST.get("effector_id", ""),
            "effector_sequence": request.POST.get("effector_sequence", ""),
            "effector_name": request.POST.get("effector_name", ""),
            "effector_description": request.POST.get("effector_description", ""),
            "effector_signal_peptide": request.POST.get("effector_signal_peptide", ""),
            "error_message": ""
        }

        # Check if effector id is unique
        if Sequence.objects.filter(effector_id=context["effector_id"]).count() != 0:
            context["error_message"] = "Effector ID '{}' already exists".format(
                context["effector_id"]
            )
            raise ValueError

        new_seq = Sequence(
            effector_id=context["effector_id"],
            effector_sequence=context["effector_sequence"],
            effector_name=context["effector_name"],
            effector_description=context["effector_description"],
            effector_signal_peptide=context["effector_signal_peptide"]
        )

        if not new_seq.effector_id:
            context["error_message"] = "Please fill in the 'effector ID' field"
            raise ValueError
        elif not new_seq.effector_sequence:
            context["error_message"] = "Please fill in the 'DNA sequence' field"
            raise ValueError

    except ValueError:
        return render(request, "database/submit.html", context)
    # Add a confirmation page
    new_seq.save()
    return HttpResponseRedirect(reverse("database:databaseViewer"))

def databaseViewer(request):
    # Obtain search terms
    context = {
        "error_message": "",
        "effector_id": request.POST.get("effector_id", ""),
        "effector_name": request.POST.get("effector_name", ""),
        "effector_signal_peptide": request.POST.get("effector_signal_peptide", "")
    }

    # Filter the data
    context["query_set"] = Sequence.objects.filter(
        effector_id__icontains=context["effector_id"],
        effector_name__icontains=context["effector_name"],
        effector_signal_peptide__icontains=context["effector_signal_peptide"]
    )

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
