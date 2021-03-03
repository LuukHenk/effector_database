from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Sequence
from .forms import SequenceForm

def index(request):
    """ Redirect to the search page, since this is our homepage """
    return HttpResponseRedirect(reverse("effector_database:search"))

def search(request):
    """
    Show the ID, name, and signal peptide of all the items in the Sequence model.
    Let the user filter items using a GET form.
    Also shows an option to view a single sequence object (see view function)
    """
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

def submit(request):
    """
    Shows a submission form for adding new sequence to the Sequence model.
    If submitted, the form will be directed to the submitted page.
    """
    form = SequenceForm(label_suffix='')
    return render(request, "effector_database/submit.html", {"form": form})

def submitted(request):
    """
    Processing a sequence submission for the Sequence model.
    Shows by Djano generated error messages on the same page if the form is incorrect.
    Redirects to the search page with a success message if the form is correct.
    """
    if request.method == "POST":
        form = SequenceForm(request.POST, label_suffix='')

        if form.is_valid():
            form.save()
            message = "Succesfully added '{}'".format(form.cleaned_data['effector_id'])
            messages.success(request, message)
            return HttpResponseRedirect(reverse("effector_database:search"))

    else: # No post request
        form = SequenceForm(label_suffix='')

    return render(request, "effector_database/submit.html", {"form": form})

def view(request, effector_id):
    """
    Show information about a single sequence from the Sequence model using it's primary key
    'effector_id'. If this fails, return to the index page (search page).
    """
    # Try to show the effector id
    try:
        context = {"sequence_obj": get_object_or_404(Sequence, pk=effector_id)}
        return render(request, "effector_database/view.html", context)

    # If an error occurs, return to the search page
    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(effector_id)
        messages.error(request, error_message)

    return HttpResponseRedirect(reverse("effector_database:search"))

def delete(request, effector_id):
    """
    Try to delete selected sequence from the Sequence model using it's primary key 'effector_id'.
    If this fails, return to the index page (search page).
    """

    # Try to delete the object
    try:
        Sequence.objects.get(pk=effector_id).delete()
        message = "Succesfully deleted sequence with effector ID '{}'".format(effector_id)
        messages.success(request, message)

    # If an error occurs, return to the search page
    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(effector_id)
        messages.error(request, error_message)

    return HttpResponseRedirect(reverse("effector_database:search"))

def update(request, effector_id):
    """
    Shows update form for a single sequence from the Sequence model using it's primary key
    'effector_id'. If the form is submitted, it will be directed to the 'updated' function.
    If not, it will return to the index page (search page).
    """

    # Create and render the effector id form.
    # the effector_id is used when directed to another page
    try:
        context = {
            "form": SequenceForm(instance=get_object_or_404(Sequence, pk=effector_id)),
            "effector_id": effector_id,
        }
        return render(request, "effector_database/update.html", context)

    # If an error occurs, return to the search page
    except ObjectDoesNotExist:
        error_message = "ERROR - Sequence with effector ID '{}' does not exists".format(effector_id)
        messages.error(request, error_message)

    return HttpResponseRedirect(reverse("effector_database:search"))

def updated(request, effector_id):
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
                return render(request, "effector_database/view.html", context)
        else: # No changes made
            return render(request, "effector_database/view.html", context)

    # Render standard context if nothing had been changed
    return render(request, "effector_database/update.html", context)
