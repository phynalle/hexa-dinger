from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.


def intro2(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def intro(request):
	return render_to_response('intro.html')