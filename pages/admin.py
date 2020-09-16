from django.contrib import admin
from .models import City


# Register your models here.
class CityAdmin(admin.ModelAdmin):
	list_display = ('city_name', 'city_county',)
	search_fields = ('city_name',)
	prepopulated_fields = {'city_slug': ('city_name',)}


admin.site.register(City, CityAdmin)
