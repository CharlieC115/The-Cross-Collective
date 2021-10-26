from django.shortcuts import render, get_object_or_404
from .models import Camp

# Create your views here.


def all_camps(request):
    """ A view to show all upcoming camps """

    camps = Camp.objects.all()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            camps = camps.filter(category__name__in=categories)

    context = {
        'camps': camps,
    }

    return render(request, 'camps/camps.html', context)


def camp_details(request, camp_id):
    """ A view to show camp details of a selected camp """

    camp = get_object_or_404(Camp, pk=camp_id)

    # if request.GET:
    #     if 'category' in request.GET:
    #         categories = request.GET['category'].split(',')
    #         camps = camps.filter(category__name__in=categories)

    context = {
        'camp': camp,
    }

    return render(request, 'camps/camp_details.html', context)
