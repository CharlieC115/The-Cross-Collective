from django.conf import settings
from django.shortcuts import get_object_or_404
from camps.models import Camp


def bag_contents(request):
    """ Context processor for shopping bag """

    bag_items = []
    total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        camp = get_object_or_404(Camp, pk=item_id)
        total += quantity * camp.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'camp': camp,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context