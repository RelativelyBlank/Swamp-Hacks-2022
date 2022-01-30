import googlemaps
import pandas as pd
import requests, os
from urllib.parse import urlencode

api_key = 'AIzaSyBluRCVit_GL-1T7B_lKyKOX1cjvTObV7Q'
map_client = googlemaps.Client(api_key)


def getLocationImage(location):
    # turn location into lat/long
    geocode_result = map_client.geocode(location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    response = map_client.places(
        location=(lat, lng),
        query = location,
    )
    results = response['results']
    # df = pd.DataFrame(results)
    # df.to_excel('list lol.xlsx', index=False)
    lol = map_client.place(results[0]['place_id'])
    # df = pd.DataFrame([lol['result']])
    # df.to_excel('list lol2.xlsx', index=False)
    photo_reference = lol['result']['photos'][0]['photo_reference']
    # download the image using places_photo and photo_reference
    photo = map_client.places_photo(photo_reference, max_width=1000, max_height=1000)
    # save the image to disk
    with open('imgs/{}.jpg'.format(location), 'wb') as photo_file:
        with open('../hacks_react/src/assets/{}.jpg'.format(location), 'wb') as photo_file2:
            for chunk in photo:
                if chunk:
                    photo_file.write(chunk)
                    photo_file2.write(chunk)
    return os.path.abspath('../hacks_react/src/assets/{}.jpg'.format(location))

def getLocationReviews(location):
    # turn location into lat/long
    geocode_result = map_client.geocode(location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    response = map_client.places(
        location=(lat, lng),
        query = location,
    )
    results = response['results']
    # df = pd.DataFrame(results)
    # df.to_excel('list lol.xlsx', index=False)
    place_id = results[0]['place_id']
    place_data = map_client.place(place_id, language='en')['result']

    # check if reviews exist
    if 'reviews' in place_data:
        # get reviews
        reviews = place_data['reviews']
    else:
        reviews = []

    print(reviews)
    return reviews




# getLocationReviews('Whitney Museum of American Art')

# getLocationImage('New York, NY')