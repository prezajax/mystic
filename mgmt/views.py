# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.template import loader
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.template.loader import render_to_string
# Create your views here.
from django.http import HttpResponse
from  mgmt.models import *

def upload(request):
	template = loader.get_template('mgmt/upload.html')
	return HttpResponse(template.render(dict(), request))
def edit(request,page_id):
	print 'fuck'
	page = Content.objects.filter(id=page_id)[0]
	context = dict()
	context['page'] = page
	template = loader.get_template('mgmt/edit.html')
	return HttpResponse(template.render(context, request))
def uploadImages(request,page_id):
	if request.method == "POST":
		img = request.FILES.get('fileToUpload')
		print img
		print page_id
	page = Content.objects.filter(id=page_id)[0]
	context = dict()
	context['page'] = page
	template = loader.get_template('mgmt/uploadImage.html')
	return HttpResponse(template.render(context, request))
def uploadContent(request):
	print request
	print "post"
	print request.POST
	newPage = Content()
	newPage.title =  request.POST["title"]
	newPage.mainText =  request.POST["mainText"]
	newPage.save()
	print 'saved'

def pages(request):
	pages =  (Content.objects.all())
	print pages[0].title
 	template = loader.get_template('mgmt/viewPages.html')
 	context = dict()
 	context["pages"] = pages
 	return HttpResponse(template.render(context, request))



# Create your views here.
