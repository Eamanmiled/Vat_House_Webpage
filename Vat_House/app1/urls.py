from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('app1/about.html', views.about, name='about'),
    path('app1/food.html', views.food, name='food'),
    path('app1/location', views.location, name='location'),
    path('app1/whisky', views.whisky, name='whisky'),
    path('app1/entertainment', views.entertainment, name='entertainment'),
]