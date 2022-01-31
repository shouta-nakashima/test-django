from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World Django")

# Create your views here.
