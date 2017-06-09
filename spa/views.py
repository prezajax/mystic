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

	title = "Facelifts"
	desc = "This revolutionary treatment performed in four layers will change the image of your skin in just one application."
	image = static("back.jpg")

	title2 = "LED Treatment"
	desc2 = "Increase new tissue growth, stimulate collagen production and reduce fine lines and wrinkles."
	image2 = static("room.jpg")
	image3 = static("head.jpg")
	imageContent = getImageWithText(image)
	imageContent2 = getImageWithText(image2)
	imageContent3 = getImageWithText(image3)
	text = getTitleBlock(title,desc)
	content = getPhotoBlockComponent(image,"True",text)

	text2 = getTitleBlock(title2,desc2)
	content2 = getPhotoBlockComponent(image2,"True",text2)

	context = {"photoBlock":imageContent,"photoBlock2":imageContent2,"photoBlock3":imageContent3}
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
	text =  getTextBlock(description,title,skinTypes,peelTypes)
	content = getPhotoBlockComponent(image,imageOnLeftSide,text)
	image2 = static("a3.jpg")
	content2 = getPhotoBlockComponent(image2,"False",text)
	image3 = static("a4.jpg")
	content3 = getPhotoBlockComponent(image3,"True",text)
	image4 = static("a5.jpg")
	content4 = getPhotoBlockComponent(image4,"False",text)
	context = {"photoBlock":[content,content2,content3,content4]}
	template = loader.get_template('spa/services.html')
	return HttpResponse(template.render(context, request))
def getPhotoBlockComponent(image,imageOnLeftSide,textComponent):
	imageContext = {"imagePath":image,"imageOnLeftSide":imageOnLeftSide,"text":textComponent}
	content = render_to_string('spa/imageTextBlock.html', imageContext)
	return content
def getTextBlock(desc,title,skinTypes,peelTypes):
	imageContext = {"description":desc,"title":title,"skinTypes":skinTypes,"peelTypes":peelTypes}
	content = render_to_string('spa/textbox.html', imageContext)
	return content
def getTitleBlock(title,desc):
	imageContext = {"description":desc,"title":title}
	content = render_to_string('spa/titleTextBox.html', imageContext)
	return content
def getImageWithText(image):
	imageContext = {"imagePath":image}
	content = render_to_string('spa/photoWithText.html', imageContext)
	return content

