from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

class BaseModel(models.Model):
	created_date  = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True


class Image(BaseModel):
	name = models.CharField(max_length=255, blank=False, null=False)
	image = models.ImageField(upload_to='media/images')
	
	# Below the mandatory fields for generic relation
	content_type 	= models.ForeignKey(ContentType, on_delete=models.CASCADE)
	object_id 		= models.PositiveIntegerField()
	content_object	= GenericForeignKey('content_type', 'object_id')
	
	comment			= models.TextField(default="", blank=True)
	
	
	#####
	#
	# Add following line to your related Model to include an image Field
	#
	#####
	#
	#  image			= GenericRelation(_lib.models.Image)
	#
	#####

