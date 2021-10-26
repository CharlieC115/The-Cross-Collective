from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_camps, name='camps'),
    path('<camp_id>', views.camp_details, name='camp_details'),
]
