import requests
from restaurant_sourse import settings


from geopy.geocoders import GoogleV3

def get_location(address):
    geolocator = GoogleV3(api_key=settings.GOOGLE_MAPS_API_KEY)

    location = geolocator.geocode(address)

    if location:
        return (location.latitude, location.longitude)
    else:
        return (None, None)