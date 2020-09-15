from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
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


def places(request):
	cities = City.objects.all()

	paginator = Paginator(cities, 6)
	page = request.GET.get('page')
	paged_cities = paginator.get_page(page)

	context = {
		'cities': paged_cities
	}

	return render(request, 'pages/places.html', context)


def place(request, city_name):
	city = get_object_or_404(City, pk=city_name)

	context = {
		'city': city
	}

	return render(request, 'pages/place.html', context)
