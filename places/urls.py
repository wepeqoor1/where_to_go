from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_places_map, name='places'),
    path('<int:place_id>', views.get_place_id, name='place_id'),
]
