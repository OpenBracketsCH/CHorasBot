import requests

def update_opening_hours(osm_element_id, new_opening_hours):
    overpass_url = "https://api.openstreetmap.org/api/0.6/changeset/create"
    changeset_tags = {'comment': 'Updated opening hours'}

    # Erstellen Sie einen Änderungssatz (changeset) für die Aktualisierung
    changeset_payload = f'<osm><changeset>{changeset_tags_xml(changeset_tags)}</changeset></osm>'
    response = requests.put(overpass_url, data=changeset_payload, headers=get_osm_auth_headers())

    changeset_id = response.text

    # Aktualisieren Sie die Öffnungszeiten des Elements
    overpass_url = f"https://api.openstreetmap.org/api/0.6/node/{osm_element_id}"

    element_payload = f'<osm><node id="{osm_element_id}" changeset="{changeset_id}"><tag k="opening_hours" v="{new_opening_hours}"/></node></osm>'
    response = requests.put(overpass_url, data=element_payload, headers=get_osm_auth_headers())

    return response.text

def changeset_tags_xml(tags):
    return ''.join([f'<tag k="{k}" v="{v}"/>' for k, v in tags.items()])

def get_osm_auth_headers():
    # Fügen Sie hier Ihren OpenStreetMap Benutzernamen und Ihr Passwort ein
    username = 'Ihr_Benutzername'
    password = 'Ihr_Passwort'

    auth = requests.auth.HTTPBasicAuth(username, password)
    headers = {'Content-Type': 'application/xml'}

    return {'Authorization': 'Basic ' + auth.token, **headers}

# Beispielaufruf
osm_element_id_to_update = 1234567890  # Ersetzen Sie dies durch die tatsächliche OSM-ID des Elements
new_opening_hours = "Mo-Fr 09:00-18:00"

response = update_opening_hours(osm_element_id_to_update, new_opening_hours)

print(response)
