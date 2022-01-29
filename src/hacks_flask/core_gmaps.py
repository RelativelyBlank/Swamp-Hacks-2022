import googlemaps
import pandas as pd

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
    with open('{}.jpg'.format(location), 'wb') as photo_file:
        for chunk in photo:
            if chunk:
                photo_file.write(chunk)

getLocationImage('New York, NY')