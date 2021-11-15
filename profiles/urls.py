from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('booking_history/<order_number>', views.booking_history, name='booking_history'),
]
