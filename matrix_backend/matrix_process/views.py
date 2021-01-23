from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import matplotlib.pyplot as plt

@csrf_exempt
def process_image(request):
    image = plt.imread(request.FILES['media'])
    return HttpResponse(status=200)
