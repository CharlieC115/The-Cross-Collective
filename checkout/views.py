from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings

# # Added for Webhooks - Trying a different way for webhooks to work
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt


from .forms import OrderForm
from .models import Order, OrderLineItem
from camps.models import Camp
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'postcode': request.POST['postcode'],
            'contact_number': request.POST['contact_number'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    camp = Camp.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        camp=camp,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Camp.DoesNotExist:
                    order.delete()
                    return redirect(reverse('bag_view'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
    else:
        bag = request.session.get('bag', {})
        if not bag:
            return redirect(reverse('camps'))

        current_bag = bag_contents(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'first_name': profile.default_first_name,
                'last_name': profile.default_last_name,
                'email': profile.default_email,
                'postcode': profile.default_postcode,
                'contact_number': profile.default_contact_number,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderFrom()
    else:
        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ view to handle successful checkouts """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_first_name': order.first_name,
                'default_last_name': order.last_name,
                'default_email': order.email,
                'default_contact_number': order.contact_number,
                'default_postcode': order.postcode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

# Trying a different way for webhooks to work
# @csrf_exempt
# def webhook_received(request):
#     if request.method == 'POST':
#         webhook_secret = settings.STRIPE_WEBHOOK_KEY
#         request_data = json.loads(request.body)

#     return JsonResponse({'status': 'success'})
