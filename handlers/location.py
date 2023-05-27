from geopy.geocoders import Nominatim

geolocator = None

def init():
    global g, geolocator
    geolocator = Nominatim(user_agent="geoapiExercises")

def get_location(long, lat):
    global geolocator
    
    long = str(long)
    lat = str(lat)
    location = geolocator.reverse(long+","+lat)
    return location.address