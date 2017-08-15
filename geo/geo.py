import requests
import geo.geoconfig
import importlib.util
spec = importlib.util.spec_from_file_location("google.key", "~/.google_key")
key = importlib.util.module_from_spec(spec)
spec.loader.exec_module(key)

class Geo:

    def get_lat_lon(self, address):

        url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=' + google_api_key
        print(url)


Geo().get_lat_lon("")