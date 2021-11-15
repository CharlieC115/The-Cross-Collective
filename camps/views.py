from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Camp
from .forms import CampForm

# Create your views here.


def all_camps(request):
    """ A view to show all upcoming camps """

    camps = Camp.objects.all().order_by('start_date')

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


@login_required
def add_camp(request):
    """ A view where admin/staff can add a camp to the bookings """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CampForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_camp'))
    else:
        form = CampForm()

    template = 'camps/add_camp.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_camp(request, camp_id):
    """ A view to allow admin/staff to edit camp details """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    camp = get_object_or_404(Camp, pk=camp_id)

    if request.method == 'POST':
        form = CampForm(request.POST, request.FILES, instance=camp)
        if form.is_valid():
            form.save()
            return redirect(reverse('camp_details', args=[camp.id]))
    else:
        form = CampForm(instance=camp)

    template = 'camps/edit_camp.html'
    context = {
        'form': form,
        'camp': camp,
    }

    return render(request, template, context)


@login_required
def delete_camp(request, camp_id):
    """ Function to delete a camp from the site """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    camp = get_object_or_404(Camp, pk=camp_id)
    camp.delete()
    return redirect(reverse('camps'))
