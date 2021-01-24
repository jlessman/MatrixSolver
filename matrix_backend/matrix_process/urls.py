from django.urls import path

from .views import *

urlpatterns = [
    path('raw/', process_image),
    path('determinant/', determinant),
    path('eigenvalue/', eigenvalue),
    path('systemOfEquations/',solve),
]
