# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse

def index(request):
	template = loader.get_template('spa/index.html')
	context = {}
	return HttpResponse(template.render(context, request))
def about(request):
	template = loader.get_template('spa/about.html')
	context = {}
	return HttpResponse(template.render(context, request))
def services(request):
	template = loader.get_template('spa/services.html')
	context = {}
	return HttpResponse(template.render(context, request))
