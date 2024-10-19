from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path('reviews', views.reviews, name='reviews'),
    path('contacts', views.contacts, name='contacts'),
    path('personal_data', views.personal_data, name='personal_data')
]
