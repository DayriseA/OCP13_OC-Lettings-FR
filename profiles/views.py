"""Views for the profiles app."""

import logging
from django.shortcuts import render, redirect
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """The profiles app index view, which lists all existing profiles."""
    try:
        profiles_list = Profile.objects.all()
    except Exception:
        logger.exception("An error occurred in the profiles list retrieval.")
        return redirect("index")

    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Render the details of a profile specified by its username."""
    # For pedagogical purposes, we don't use a try/except block here so we can cause
    # an error easily for demonstration purposes.
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
