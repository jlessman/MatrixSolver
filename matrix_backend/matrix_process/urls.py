from django.urls import path

from .views import *

urlpatterns = [
    path('raw/', process_image)
]
