from __future__ import unicode_literals

from django.db import models
from _lib.models import BaseModel

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Product(BaseModel):
	name			= models.CharField(max_length = 100, null=False, blank=False)
	#machines 		= models.ManyToManyField('hardware.Machine', blank=True)
	comment			= models.TextField(default="", blank=True)
	
	def __unicode__(self):
		return self.name



