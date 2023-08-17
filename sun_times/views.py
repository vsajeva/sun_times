from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CoordinatesForm
from .tools import get_sun_time_from_coordinates


def get_coordinate(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CoordinatesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            sun_time = get_sun_time_from_coordinates(lat=form.cleaned_data["lat"], lng=form.cleaned_data["lng"])
            return render(
                request=request,
                template_name="coordinate.html",
                context={"form": form, "sunrise": sun_time["sunrise"], "sunset": sun_time["sunset"]},
            )

    # if a GET (or any other method) we'll create a blank form
    form = CoordinatesForm()
    return render(request, "coordinate.html", {"form": form})
