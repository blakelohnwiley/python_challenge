from lookups import geo_ip_lookup
from lookups import rdap_lookup
from parsing import parsing
from sql import query_db
import os
from utilities import argparser 
import time
from tqdm import tqdm

def populate(file_name="list_of_ips.txt"):
# The first step is to fetch the IP addresses inside the file and store them in an array.
    args = argparser.input_args()
    current_dir=os.getcwd()
    file_name=os.path.join(current_dir, "data", file_name)
    if args.debug == True:
        print("Opening file [", file_name, "]")
    ip_text=parsing.file_to_text(file_name)
    list_of_ips=parsing.parse(ip_text)
# The second step is to execute the lookups on each IP of the array
# We also need to connect to the database to insert the values as we perform the geo ip lookup
    connection_db=query_db.connect_to_database()
    query_db.execute_query("USE swimlane;", connection_db.cursor(), connection_db)
    #init progress bar
    len_of_list = len(list_of_ips)
    for i in tqdm(range(len_of_list)):
        ip = list_of_ips[i]
        geo_info=geo_ip_lookup.geo_ip_query(ip)
#        print(geo_info)
        if geo_info!=None:
            geo_ip_insert_query="INSERT INTO geo_ip(ip_address, country_code, country_name, region_code, region_name, city, zip_code, time_zone, latitude, longitude, metro_code) VALUES('"\
            +geo_info['ip']+"', '"\
            +geo_info['country_code']+"', '"\
            +geo_info['country_name']+"', '"\
            +geo_info['region_code']+"', '"\
            +geo_info['region_name']+"', '"\
            +geo_info['city']+"', '"\
            +geo_info['zip_code']+"', '"\
            +geo_info['time_zone']+"', '"\
            +str(geo_info['latitude'])+"', '"\
            +str(geo_info['longitude'])+"', '"\
            +str(geo_info['metro_code'])+"');"
        else:
            geo_ip_insert_query="INSERT INTO geo_ip(ip_address, country_code, country_name, region_code, region_name, city, zip_code, time_zone, latitude, longitude, metro_code) VALUES('"\
            +geo_info['ip']+"','','','','','','','','','','' );"
#        print(geo_ip_insert_query)
#        query_db.execute_query("USE swimlane;", connection_db.cursor(), connection_db)

        query_db.execute_query(geo_ip_insert_query, connection_db.cursor(), connection_db)
        rdap_info=rdap_lookup.rdap_query(ip)
        rdap_extract=rdap_lookup.rdap_extract(rdap_info)
        #print(rdap_extract)
        if rdap_extract!=None:
            rdap_insert_query="INSERT INTO rdap(ip_address, start_address, end_address, company_name, company_address) VALUES('"\
            +ip+"', '"\
            +rdap_extract['startAddress']+"', '"\
            +rdap_extract['endAddress']+"', '"\
            +rdap_extract['company_name']+"', '"\
            +rdap_extract['company_address'].replace("\n", " ")+"');"
        else:
            rdap_insert_query="INSERT INTO rdap(ip_address, start_address, end_address, company_name, company_address) VALUES('"\
            +ip+"','','','','');" 
#        print(rdap_insert_query)
#    connection_db.close()
        query_db.execute_query(rdap_insert_query, connection_db.cursor(), connection_db)
    connection_db.close()

def query_loop(connection):
    user_input=""
    while user_input!="exit;":
        query=input("Type in a SQL query (don't forget the ';' at the end)\n")+";"
        result=query_db.query_db(connection, query)
        try:
            parsing.display_dict(result)
        except:
            print("Unable to display the result")
        user_input=query
    print("Exiting the program")
    connection.close()
    return(0)

def main():
    args = argparser.input_args()
    ask_populate=input("Do you want to initialize the database ? (yes/no)\n")
    if ask_populate=='yes':
        print("Populating the database. This operation may take a while.")
        populate(args.filename)
        print("Population complete")
    else:
        print("Skipping the population phase")
    connection_db=query_db.connect_to_database()
    query_loop(connection_db)

if __name__=="__main__":
    main()
