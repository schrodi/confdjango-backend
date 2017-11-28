from __future__ import unicode_literals

from django.db import models
from _lib.models import BaseModel
#import cities_light


class Customer(BaseModel):
	#Foreign Keys
	#Info
	shortName   = models.CharField(max_length=10, blank=False, null=False, unique=True)
	name        = models.CharField(max_length=100, blank=False, null=False, unique=True)
	
	def __unicode__(self):
		return "[" + self.shortName + "] " + self.name

class Location(BaseModel):
	customer 			= models.ForeignKey(Customer, related_name="customerLocation_related", )
	localCompanyName 	= models.CharField(max_length = 50, blank=False, null=False)
	#country			Foreignkey via city and django-cities-light
	city 				= models.ForeignKey('cities_light.City')
	street 				= models.CharField(max_length = 50, blank=False, null=False)
	plz 				= models.CharField(max_length = 5, blank=False, null=False)
	isRZ 				= models.BooleanField()
	comment				= models.TextField(default="", null=False, blank=True)

	def __unicode__(self):
		return self.city.__str__()

class Site(BaseModel):
	customer 	= models.ForeignKey(Customer, related_name="customerSite_related")
	locations 	= models.ManyToManyField('Location', blank=True)
	# Info
		#Site_ID :  000000.000000
		#			Kunde.SiteNr
	#customID 	= models.IntegerField(blank = True)
	site_ID 	= models.CharField(max_length = 13, blank = True)
	#@property
	#def site_ID(self):
	#	return '{customer : 0 > 3}:{siteID}'.format(customer.customID, customID)
    	
	comment		= models.TextField(default="", null=False, blank=True)



	def __unicode__(self):
		return self.site_ID
		
	def save(self, *args, **kwargs):
		
		super(Site, self).save(*args, **kwargs)

		
		self.site_ID = '{customer:06d}:{site:06d}'.format(customer = self.customer.pk, site = self.pk)
		
		super(Site, self).save(*args, **kwargs)

# many to many tables
"""
class Site_Location(BaseModel):
    site 		= models.ForeignKey(Site, )
    location 	= models.ForeignKey(Location, )

class Site_Product(BaseModel):
    site = models.ForeignKey(Site, )
    product = models.ForeignKey(Product, )
"""













