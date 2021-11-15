from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_camps, name='camps'),
    path('<int:camp_id>/', views.camp_details, name='camp_details'),
    path('add/', views.add_camp, name='add_camp'),
    path('edit/<int:camp_id>/', views.edit_camp, name='edit_camp'),
    path('delete/<int:camp_id>/', views.delete_camp, name='delete_camp'),
]
