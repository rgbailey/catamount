from django.db import models


class City(models.Model):
	COUNTY_CHOICES = [
		('', 'Select County'),
		('CC', 'Chittenden County'),
		('GC', 'Grand Isle County'),
		('FC', 'Franklin County'),
	]

	city_name = models.CharField(max_length=50)
	city_county = models.CharField(max_length=30, choices=COUNTY_CHOICES, default='')
	city_description = models.TextField(blank=False)
	photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
	photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

	def __str__(self):
		return self.city_name
