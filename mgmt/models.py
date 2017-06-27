# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Content(models.Model):
	title = models.CharField(max_length=50)
	mainText = models.CharField(max_length=500)


class pageImages(models.Model):
	imageTitle = models.CharField(max_length=50)
	imageURL = models.ImageField()
	mainPage = models.ForeignKey(
        'Content',
        on_delete=models.CASCADE,
    )




# Create your models here.
