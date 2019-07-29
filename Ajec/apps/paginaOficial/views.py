from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

# Create your views here.

class home(TemplateView):
	template_name='home/home.html'

def inicio(request):
	return render(request,'base/base.html')

def index(request):
	return HttpResponse("index")


