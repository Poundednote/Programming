import urllib.request
import json


class GetInfo(object):

    def __init__(self):
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?'
        self.geourl = 'http://freegeoip.net/json'

    def get_location(self):
        url = urllib.request.urlopen(self.geourl)
        location = json.load(url)
        # tidies location into a dict with the only the important info
        location_info = {
            'lat': location['latitude'],
            'lon': location['longitude']
        }
        return location_info

    def get_weather(self, auth, location, units):
        lat = location['lat']
        lon = location['lon']
        url = urllib.request.urlopen(self.base_url +
            'lat=%s&lon=%s&units=%s&appid=%s'
            % (lat, lon, units, auth))
        weather_info = json.load(url)
        return weather_info
