from django.shortcuts import render
from django.views.generic import TemplateView

class PostView(TemplateView):
	template_name = 'home.html'

