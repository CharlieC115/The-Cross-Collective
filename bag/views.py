from django.shortcuts import render

# Create your views here.


def bag_view(request):
    """ View to return the bag page with contents """

    return render(request, 'bag/bag.html')
