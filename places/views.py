from typing import Iterator

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Place


def get_places() -> Iterator:
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


def get_places_map(request) -> render:
    places: Iterator[dict] = get_places()
    places_geo = {
      'type': 'FeatureCollection',
      'features': [
          dict(place) for place in places
      ]
    }

    return render(request, 'main_page_map.html', context={'places_geo': places_geo})


def get_place_id(request, place_id: int) -> render:
    place = get_object_or_404(Place, id=place_id)
    imgs = place.images.all()
    data = {
        'title': f'{place.title}',
        'imgs': [img.image.url for img in imgs],
        'description_short': f'{place.description_short}',
        'description_long': f'{place.description_long}',
        'coordinates': {
            'lng': f'{place.longitude}',
            'lat': f'{place.latitude}'
        }
    }

    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
