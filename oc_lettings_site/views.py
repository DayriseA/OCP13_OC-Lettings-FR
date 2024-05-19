"""Non app-specific views for the project. E.g. homepage."""

import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Render the homepage. Uses the project's level index.html template."""
    return render(request, "index.html")


def demo_logs(request):
    """For pedagogical purposes. Generate logs of different levels."""
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    # let's cause an exception
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except Exception:
        logger.exception("Exception occurred when dividing by zero. What a surprise!")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
    return render(request, "index.html")
