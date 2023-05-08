import json
from typing import Iterator

from django.shortcuts import render

from .models import Place


def get_places():
    places = Place.objects.all()

    for place in places:
        data = {
            "type": place.type,
            "geometry": {
                "type": place.geometry_type,
                "coordinates": [place.latitude, place.longitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": place.details_url
            }
        }
        yield data


def main_page_map(request):
    places: Iterator[dict] = get_places()
    places_geo = {
      'type': 'FeatureCollection',
      'features': [
          dict(place) for place in places
      ]
    }

    return render(request, 'main_page_map.html', context={'places_geo': places_geo})
