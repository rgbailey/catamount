from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from listings.models import Listing
from realtors.models import Realtor
from .models import City


def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True)
	context = {
		'listings': listings
	}
	return render(request, 'pages/index.html', context)


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)


def sell(request):
	return render(request, 'pages/sell.html')


def places(request):
	cities = City.objects.all()

	paginator = Paginator(cities, 6)
	page = request.GET.get('page')
	paged_cities = paginator.get_page(page)

	context = {
		'cities': paged_cities
	}

	return render(request, 'pages/places.html', context)


def place(request, city_slug):
	city = get_object_or_404(City, city_slug=city_slug.lower())

	context = {
		'city': city
	}

	return render(request, 'pages/place.html', context)
