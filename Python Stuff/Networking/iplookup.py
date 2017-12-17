from urllib.request import urlopen
import json

def get_info():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.loads(response)


def get_ip():
    
    ip = data['ip']
    hostname = data['hostname']
    city = data['city']
    region = data['region']
    country = data['country']
    loc = data['loc']
    org = data['org']
    zipcode = data['postal']

    return 