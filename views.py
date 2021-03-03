from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import UpdateView

from .models import Sequence
from .forms import SequenceForm

def index(request):
    return HttpResponseRedirect(reverse("effector_database:search"))

def submit(request):
    form = SequenceForm(label_suffix='')
    return render(request, "effector_database/submit.html", {"form": form})

def submitted(request):
    if request.method == "POST":
        form = SequenceForm(request.POST, label_suffix='')

        if form.is_valid():
            form.save()
            message = "Succesfully added '{}'".format(form.cleaned_data['effector_id'])
            messages.success(request, message)
            return HttpResponseRedirect(reverse("effector_database:search"))

    else:
        form = SequenceForm(label_suffix='')

    return render(request, "effector_database/submit.html", {"form": form})

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
    print(context)
    return render(request, "effector_database/search.html", context)

def itemViewer(request, effector_id):
    context = {
        "sequence_obj": get_object_or_404(Sequence, pk=effector_id)
    }
    return render(request, "effector_database/itemViewer.html", context)


def deleteItem(request, effector_id):
    try:
        Sequence.objects.get(pk=effector_id).delete()
        message = "Succesfully deleted sequence with effector ID '{}'".format(effector_id)
        messages.success(request, message)

    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(effector_id)
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("effector_database:search"))
    except:
        error_message = "ERROR - Unknown error"
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("effector_database:search"))


    return HttpResponseRedirect(reverse("effector_database:search"))

def editItem(request, effector_id):
    """ """
    try:
        context = {
            "form": SequenceForm(instance=Sequence.objects.get(pk=effector_id)),
            "effector_id": effector_id,
        }
        return render(request, "effector_database/editItem.html", context)

    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(effector_id)
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("effector_database:search"))

    return HttpResponseRedirect(reverse("effector_database:search"))

def updatedItem(request, effector_id):
    """
    Process content update of a single sequence from the Sequence model using it's primary key
    'effector_id'. Unable to update the effector_id, since this breaks current url.
    """

    # Generate standard context
    context = {
        "effector_id": effector_id,
        "sequence_obj": get_object_or_404(Sequence, pk=effector_id),
    }
    context["form"] = SequenceForm(instance=context["sequence_obj"], label_suffix='')

    # Check if new data has been submitted
    if request.method == "POST":
        form = SequenceForm(request.POST, instance=context["sequence_obj"], label_suffix='')

        if form.has_changed():
            # Don't let user change the effector ID
            if "effector_id" in form.changed_data:
                messages.error(request, "Only admin change the effector ID")
            elif form.is_valid():
                form.save()
                message = "Succesfully edited effector ID '{}'".format(effector_id)
                messages.success(request, message)
                return render(request, "effector_database/itemViewer.html", context)
        else: # No changes made
            return render(request, "effector_database/itemViewer.html", context)

    # Render standard context if nothing had been changed
    return render(request, "effector_database/editItem.html", context)
