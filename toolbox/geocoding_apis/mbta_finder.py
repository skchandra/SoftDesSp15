""" Shivali Chandra
3/29/15
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    place_name = place_name.replace(" ","%20")
    url = GMAPS_BASE_URL+place_name
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    latitude = response_data["results"][0]["geometry"]["location"]["lat"]
    longitude = response_data["results"][0]["geometry"]["location"]["lng"]
    return latitude,longitude

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url_mbta = MBTA_BASE_URL+"?api_key="+MBTA_DEMO_API_KEY+"&lat="+str(latitude)+"&lon="+str(longitude)+"&format=json"
    f = urllib2.urlopen(url_mbta)
    response_text_mtba = f.read()
    response_data_mtba = json.loads(response_text_mtba)
    station_name = response_data_mtba["stop"][0]["stop_name"]
    distance = response_data_mtba["stop"][0]["distance"]
    return station_name, distance

def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat = get_lat_long(place_name)[0]
    lng = get_lat_long(place_name)[1]
    return get_nearest_station(lat,lng)

print find_stop_near("Fenway Park")

