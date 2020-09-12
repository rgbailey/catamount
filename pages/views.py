from django.shortcuts import render
from listings.models import Listing
from .models import City


def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	context = {
		'listings': listings
	}
	return render(request, 'pages/index.html', context)


def about(request):
	return render(request, 'pages/about.html')


def places(request, city_name):
	city = City.objects.get(city_name)2
	context = {
		'city': city
	}
	return render(request, 'pages/places.html', context)
