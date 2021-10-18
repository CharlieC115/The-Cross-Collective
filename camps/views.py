from django.shortcuts import render
from .models import Camp

# Create your views here.


def all_camps(request):
    """ A view to show all upcoming camps """

    camps = Camp.objects.all()

    context = {
        'camps': camps,
    }

    return render(request, 'camps/camps.html', context)
