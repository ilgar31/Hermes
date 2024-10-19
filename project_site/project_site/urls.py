from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .views import page_not_found_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
]

handler404 = page_not_found_view

