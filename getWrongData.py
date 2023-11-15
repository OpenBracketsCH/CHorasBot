import requests

def search_places_with_opening_hours(opening_hours):
    overpass_url = "http://overpass-api.de/api/interpreter"
    query = f'[out:json];node["opening_hours"="{opening_hours}"];out;'

    response = requests.get(overpass_url, params={'data': query})
    data = response.json()

    places = []
    for element in data['elements']:
        if 'tags' in element:
            place_name = element['tags']['name'] if 'name' in element['tags'] else 'Unnamed Place'
            places.append(place_name)

    return places

# Beispielaufruf
opening_hours_to_search = "Mo-Fr 09:00-17:00"
result = search_places_with_opening_hours(opening_hours_to_search)

print(f"Places with opening hours '{opening_hours_to_search}': {result}")
