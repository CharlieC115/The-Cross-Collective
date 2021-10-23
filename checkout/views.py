from django.shortcuts import render, redirect, reverse

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        return redirect(reverse('camps'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JeJgeJTmNqThVZM2M67Wz1d1nPyT452tbtxC5VNYDoLfRIWtIdQn7EXln3LRHWMqdKNZtVEkGCYrNNOB42K41LB00NgOQ0nzp',
    }

    return render(request, template, context)
