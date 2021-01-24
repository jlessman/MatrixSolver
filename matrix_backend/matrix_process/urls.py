<<<<<<< HEAD
from django.urls import path

from .views import *

urlpatterns = [
    path('raw/', process_image),
    # path('test2/', Test),
]
=======
from django.urls import path

from .views import *

urlpatterns = [
    path('raw/', process_image),
    path('determinant/', determinant),
    path('eigenvalue/', eigenvalue),
    path('systemOfEquations/',solve),
]
>>>>>>> 54655c06ad6a703bdaa50b636a49e787dcbaad35
