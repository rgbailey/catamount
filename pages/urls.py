from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('sell-with-catamount/', views.sell, name='sell'),
	path('vermont-communities/', views.places, name='places'),
	path('vermont-communities/<str:city_slug>', views.place, name='place'),

]
