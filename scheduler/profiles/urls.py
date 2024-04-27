from django.urls import path
from profiles import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('booking', views.booking, name='booking'),
    path('schedule', views.schedule, name='schedule'),
]