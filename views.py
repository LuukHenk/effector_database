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
    return render(request, "effector_database/search.html", context)

def itemViewer(request, item_name):
    context = {
        "item": get_object_or_404(Sequence, pk=item_name)
    }
    return render(request, "effector_database/itemViewer.html", context)


def deleteItem(request, item_name):
    try:
        Sequence.objects.get(effector_id=item_name).delete()
        message = "Succesfully deleted sequence with effector ID '{}'".format(item_name)
        messages.success(request, message)

    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(item_name)
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("effector_database:search"))
    except:
        error_message = "ERROR - Unknown error"
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("effector_database:search"))


    return HttpResponseRedirect(reverse("effector_database:search"))

def editItem(request, item_name):
    try:
        context = {
            "form": SequenceForm(instance=Sequence.objects.get(effector_id=item_name)),
            "item_name": item_name,
        }
        return render(request, "effector_database/editItem.html", context)

    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(item_name)
        messages.error(request, error_message)
        return HttpResponseRedirect(reverse("effector_database:search"))

    return HttpResponseRedirect(reverse("effector_database:search"))

def updatedItem(request, item_name):
    context = {
        "item_name": item_name,
        "item": get_object_or_404(Sequence, pk=item_name),
    }

    if request.method == "POST":
        form = SequenceForm(request.POST, instance=context["item"], label_suffix='')

        if form.has_changed():
            # Make user unable to overwrite already existing effector ID
            if "effector_id" in form.changed_data:
                new_effector_id = form["effector_id"].value()
                for existing_seq in Sequence.objects.all():
                    if existing_seq.effector_id == new_effector_id:
                        form.add_error("effector_id", "Sequence with this Effector id already exists.")
            # Check if the edit is valid
            if form.is_valid():
                form.save()
                message = "Succesfully edited effector ID '{}'".format(form.cleaned_data['effector_id'])
                messages.success(request, message)
                return render(request, "effector_database/itemViewer.html", context)

        # If no changes were made
        else:
            return render(request, "effector_database/itemViewer.html", context)

    # If there is no post request
    else:
        form = SequenceForm(instance=context["item"], label_suffix='')

    context["form"] = form
    return render(request, "effector_database/editItem.html", context)
