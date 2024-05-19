"""Views for the lettings app."""

import logging
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """The lettings app index view, which lists all lettings objects."""
    try:
        lettings_list = Letting.objects.all()
    except Exception:
        logger.exception("An error occurred in the lettings list retrieval.")
        return redirect("index")

    # Not very useful, but for demonstration purposes
    logger.info("Lettings list retrieved successfully.")
    logger.debug(f"lettings_list length: {len(lettings_list)}")

    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Render the details of a letting object specified by its id."""
    try:
        letting = Letting.objects.get(id=letting_id)
    except ObjectDoesNotExist:
        logger.exception("The specified letting does not exist.")
        raise Http404("404: Letting not found.")
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
