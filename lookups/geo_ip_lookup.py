import requests
import json

# This file contains the required fuction to perform a geo ip lookup
# The function takes an IP address as input, will perform a GET request to freegeoip.app and parse the output as a python dictionary

def geo_ip_query(ip_address):
    api_url  = "https://freegeoip.app/json/{}".format(ip_address)
    headers = {
    'accept': "application/json",
    'content-type': "application/json"}
    response = requests.get(api_url,headers=headers)
    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        print(response.content )
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 200:
        geo_query = json.loads(response.content.decode ('utf-8'))
        return geo_query
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None