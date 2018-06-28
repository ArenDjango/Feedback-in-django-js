from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.


def home(request):
	return render(request, 'home.html')

def post(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		text = request.POST.get('text', None)
		# name = 'name'
		# text = 'text'
		c = FeetBack.objects.create(name=name, text=text)
	return JsonResponse({ 'name': name, 'text': text })