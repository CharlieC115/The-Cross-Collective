import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from camps.models import Camp

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=16, null=False, blank=False)
    last_name = models.CharField(max_length=16, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=16, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    postcode = models.CharField(max_length=8, null=False, blank=False)

    def _generate_order_number(self):
        """ Generate a random, uniq order number using uuid """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update total everytime a line item is added """
        self.total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number if it hasn't been set already. """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    camp = models.ForeignKey(Camp, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Override the original save method to set the lineitem total and update the order total. """
        self.lineitem_total = self.camp.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Thank you for booking {self.camp.name}. You order number is {self.order.order_number}'
