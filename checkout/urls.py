from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    # Trying a different way to make to webhooks work
    # path('whweb/', views.webhook_received, name='webhookweb'),
]
