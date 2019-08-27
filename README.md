# IP Lookup
# Motivation
Create a program that will read a given set of IPs, perform Geo IP and RDAP lookups, and accept a query to filter results.
# Screenshots 
# Tech/framework used  
# Features
This program will read a given set of IPs, perform Geo IP and RDAP lookups, and accept a query to filter results. Each component is decoupled from the others and easy to use. There are five componenets to this application:
- Lookup
    - Geolocation
    - RDAP
- Parsing
- SQL
- Utilities
- Data

# Structure

├── data
│   └── list_of_ips.txt
├── LICENSE
├── lookups
│   ├── geo_ip_lookup.py
│   └── rdap_lookup.py
├── main_program.py
├── parsing
│   ├── __init__.py
│   └── parsing.py
├── README.md
├── requirements.txt
├── sql
│   ├── init_db.sql
│   ├── __init__.py
│   ├── init_user.sql
│   └── query_db.py
└── utilities
    ├── argparser.py
    └── __init__.py
    
## Lookup
This modlue contains both the geolocation and rdap query.
### Geolocation Query
This submodule contains the required function to perform a geolocation ip lookup. The function takes an IP address as input, will perform a GET request to freegeoip.app and parse the output as a python dictionary.
### RDAP Query
This submodule contains the necessary functions to perform a RDAP lookup. The rdap_query function takes an IP address as input and returns a dictionary will all the retreive information. 
Seeing as the RDAP lookup returns a lot of information, the extract function filters this data and selects only the relevant information (the values have been chosen a bit arbitrarily and can be modified to fit the needs of the user).
## Parsing
This module contains the functions necessary to take a text file as input and extract the IP addresses from it then return a list of these IP addresses. The function file_to_text will simply open a file and return a big string with the contents of the file.
## SQL
This folder contains all the necessary modules and functions to interact with the database using python. By default it will connect to the database created with the scripts provided.
The scripts provided create the user,database,tables, table schemas.
## Utilities
This module allows the user to pass two input arguments: -d and -f. The -d flag is for debugging and the -f is the file containing unstrucuted data. 
## Data
This folder contains only one file list_of_ips.txt. If the user wishses to use another text file, all they have to do is place it in this directory. 

# Code Example 

# Installation 
Provide step by step series of examples and explanations about how to get a development env running.
- Install the MySQL server by using the Linux Package Manager
- sudo apt-get update 
- sudo apt-get install mysql-server git python3-pip
- mysql_secure_installation (Maybe)
- This utility prompts you to define the mysql root password and other security-related options, including removing remote access to the root user and setting the root password.
- git clone https://github.com/blakelohnwiley/python_challenge.git
- change directory to sql/
- mysql -u root -p < init_user.sql 
- mysql -u geordap -p < init_db.sql 
= change back one directory by inputing cd ..
- pip3 install -r requirements 
# Tests 
Describe and show how to run the tests with code examples.
# How to USe
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.
# License
MIT License
