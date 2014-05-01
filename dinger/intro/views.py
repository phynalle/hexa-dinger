from django.shortcuts import render
from django.shortcuts import render_to_response

def intro(request):
	return render_to_response('jumbotron.html')
