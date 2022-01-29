# make a function that returns the image of a location on google maps
# import googlemaps
from googlemaps import Client
from googlemaps.geocoding import geocode

gmaps = Client(key="AIzaSyBluRCVit_GL-1T7B_lKyKOX1cjvTObV7Q")

def getLocationImage(location):
    global gmaps
    # geocode the location
    result = gmaps.geocode(location)
    # get the lat and lng of the location
    lat = result[0]['geometry']['location']['lat']
    lng = result[0]['geometry']['location']['lng']
    # get the image from the places api
    image = gmaps.places_photo(location, max_width=1000, max_height=1000)


im = getLocationImage("New York")
print(im)