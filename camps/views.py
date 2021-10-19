from django.shortcuts import render
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
