# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.template.loader import render_to_string
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
	image = static("a2.jpg")
	imageOnLeftSide = "True"
	description = "This revolutionary treatment performed in four layers will change the image of your skin in just one application. Vitamin C, Glycolic Acid, and gentle but highly effective enzymes speed up cellular turnover and brighten, tighten, and lighten your skin in just one treatment. Revitalize dry, dull, aging skin with this Vitamin C enriched hydrating facial."
	title = "The Signature Facelift"
	content = getPhotoBlockComponent(image,imageOnLeftSide,description,title)

	contnet2 = getPhotoBlockComponent(image,"False",description,title)

	context = {"photoBlock":content,"secondBlock":contnet2}
	template = loader.get_template('spa/services.html')
	return HttpResponse(template.render(context, request))

def getPhotoBlockComponent(image,imageOnLeftSide,desc,title):
	imageContext = {"imagePath":image,"description":desc,"imageOnLeftSide":imageOnLeftSide,"title":title}
	content = render_to_string('spa/imageTextBlock.html', imageContext)
	return content
