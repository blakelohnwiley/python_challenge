# This file contains the functions necessary to take a text file as input and extract the IP addresses from it then return a list of these IP addresses. 
# file_to_text will simply open a file and return a big string with the content of the file.

import re

def parse(ip_text):
    list_of_ips=re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', ip_text)
    return(list_of_ips)

def file_to_text(file_name):
    try:
        ip_file=open(file_name, 'r')
        ip_text=ip_file.read()
        return(ip_text)
    except:
        print("Unable to open the file", file_name)

def display_dict(dictionary):
# This function takes a dictionary as input and displays it in a prettier way than the regular print(<dict>)
    for line in dictionary:
        keys=list(line.keys())
        for i in range(len(keys)):
            #print(line[keys[0]].ljust(20), line[keys[1]].l    just(20), "\n")
            print(keys[i]," = ", line[keys[i]], end=" | ")
        print("\n")

def main(file_name):
    ip_text=file_to_text(file_name)
    print(ip_text)
    list_of_ips=parse(ip_text)
    print(list_of_ips)
    print(len(list_of_ips))

if __name__=="__main__":
    file_name="list_of_ips.txt"
    main(file_name)
