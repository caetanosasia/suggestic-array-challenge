from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import flattens_array


urlpatterns = [
    path('admin/', admin.site.urls),
    path('flattens-array/', flattens_array, name='flattens-array'),
]
