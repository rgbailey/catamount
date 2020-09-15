from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('vermont-communities/', views.places, name='places'),
	path('vermont-communities/<slug:city_name>', views.place, name='place'),

]
