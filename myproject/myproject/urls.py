from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import normalize_array


urlpatterns = [
    path('admin/', admin.site.urls),
    path('normalize-array/', normalize_array, name='normalize-array'),
]
