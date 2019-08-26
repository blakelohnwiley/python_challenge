import requests
import json
from utilities import argparser
# This file contains the necessary functions to perform a RDAP lookup. The rdap_query function takes an IP address as input and returns a dictionary will all the retreive information.
# Seeing as the RDAP lookup returns a lot of information, the extrat function filters this data and selects only the relevant information (the values have been chosen a bit arbitrarily and can be modified to fit the needs of the user).


def rdap_query(ip_address):
    args = argparser.input_args()
    api_url = "https://rdap.arin.net/registry/ip/{}".format(ip_address)
    headers = {
    'accept': "application/json",
    'content-type': "application/json"}
    response = requests.get(api_url,headers=headers)
    if response.status_code >= 500:
        if args.debug == True:
            print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code >= 429:
        if args.debug == True:
            print ( '[!] [{0}] Too Many Requests'.format ( response.status_code ) )
            print ( "Using Alternative RDAP API Site" )
        alt_api_url = "https://www.rdap.net/ip/{}".format(ip_address)
        alt_response = requests.get(alt_api_url,headers=headers)
        rdap_query = json.loads ( response.content.decode ( 'utf-8' ) )
        return rdap_query
    elif response.status_code == 404:
        if args.debug == True:
            print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        if args.debug == True:
            print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 400:
        if args.debug == True:
            print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        if args.debug == True:
            print('[!] [{0}] Unexpected redirect.'.format(response.status_code))
        return None
    elif response.status_code == 200:
        rdap_query = json.loads(response.content.decode ('utf-8'))
        return rdap_query
    else:
        if args.debug == True:
            print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
        return None
#def rdap_extract(ip,query_response):
#    temp_dict = {}
#    temp_dict [ "startAddress" ] = query_response [ "startAddress" ]
#    temp_dict [ 'endAddress' ] = query_response [ "endAddress" ]
#    entities = query_response [ 'entities' ]
#    for entry in entities:
#        # grab value associated with vcardArray
#        temp_dictionary = entry [ 'vcardArray' ]
#        # iterate for values to retrieve
#        for values in temp_dictionary:
#            # grab nested values: company name and address
#            # update rdap dictionary with key,value
#            for value in values:
#                if "fn" in value:
#                    temp_dict [ "company_name" ] = value [ 3 ]
#                if "adr" in value:
#                    temp_dict [ "company_addrress" ] = value [ 1 ] [ 'label' ]
#    return temp_dict
def rdap_extract(query_response):
    try:
        temp_dict = {}
        temp_dict [ "startAddress" ] = query_response [ "startAddress" ]
        temp_dict [ 'endAddress' ] = query_response [ "endAddress" ]
        entities = query_response [ 'entities' ]
        for entry in entities:
            # grab value associated with vcardArray
            temp_dictionary = entry [ 'vcardArray' ]
            # iterate for values to retrieve
            for values in temp_dictionary:
                # grab nested values: company name and address
                # update rdap dictionary with key,value
                for value in values:
                    if "fn" in value:
                        temp_dict [ "company_name" ] = value [ 3 ]
                    if "adr" in value:
                        temp_dict [ "company_address" ] = value [ 1 ] [ 'label' ]
        return temp_dict
    except:
        return None
