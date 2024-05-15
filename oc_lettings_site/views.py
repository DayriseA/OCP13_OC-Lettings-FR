"""Non app-specific views for the project. E.g. homepage."""

from django.shortcuts import render


def index(request):
    """Render the homepage. Uses the project's level index.html template."""
    return render(request, "index.html")
