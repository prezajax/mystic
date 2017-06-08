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
def led(request):
	template = loader.get_template('spa/led.html')
	context = {}
	return HttpResponse(template.render(context, request))
def peels(request):
	image = static("a2.jpg")
	imageOnLeftSide = "True"
	description = "This revolutionary treatment performed in four layers will change the image of your skin in just one application. Vitamin C, Glycolic Acid, and gentle but highly effective enzymes speed up cellular turnover and brighten, tighten, and lighten your skin in just one treatment. Revitalize dry, dull, aging skin with this Vitamin C enriched hydrating facial."
	title = "The Signature Facelift"
	skinTypes = ["Rosacea","dull/tired","pregnant","dry/dehydrated","smoker’s complexion","post-microdermabrasion","post-surgery"]
	peelTypes = ["Vitamin C","Enzyme Resurfacing Solution"]

	content = getPhotoBlockComponent(image,imageOnLeftSide,description,title,skinTypes,peelTypes)
	#contnet2 = getPhotoBlockComponent(image,"False",description,title)
	image2 = static("a3.jpg")
	content2 = getPhotoBlockComponent(image2,"False",description,title,skinTypes,peelTypes)
	image3 = static("a4.jpg")
	content3 = getPhotoBlockComponent(image3,"True",description,title,skinTypes,peelTypes)
	image4 = static("a5.jpg")
	content4 = getPhotoBlockComponent(image4,"False",description,title,skinTypes,peelTypes)
	context = {"photoBlock":[content,content2,content3,content4]}
	template = loader.get_template('spa/services.html')
	return HttpResponse(template.render(context, request))

def getPhotoBlockComponent(image,imageOnLeftSide,desc,title,skinTypes,peelTypes):
	imageContext = {"imagePath":image,"description":desc,"imageOnLeftSide":imageOnLeftSide,"title":title,"skinTypes":skinTypes,"peelTypes":peelTypes}
	content = render_to_string('spa/imageTextBlock.html', imageContext)
	return content
