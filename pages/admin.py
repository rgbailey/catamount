from django.contrib import admin
from .models import City


# Register your models here.
class ListingAdmin(admin.ModelAdmin):
	list_display = ('city_name', 'city_description')


admin.site.register(City)
