from django.urls import path
from .views import add_health_record, health_record_success, your_view

urlpatterns = [
    path('add_health_record/', add_health_record, name='add_health_record'),
    path('health_record_success/', health_record_success, name='health_record_success'),
    path('your_view/', your_view, name='your_view'),
]