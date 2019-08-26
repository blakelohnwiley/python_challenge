# This file contains all the necessary functions to interact with the database using python. By default it will connect to the database created with the cripts provided.

import pymysql
import pymysql.cursors
from utilities import argparser

def sql_injection(string):
    s = [";","\"","+","*","/","%","$","--","^", "@","~","`","SELECT ", "UNION ","select", "union "]
    for i in s:
        if (i in str(string)):
            return(False)
    return(True)

def connect_to_database(host='localhost', user='swimlane', password='swimlane', db='swimlane'):
    args = argparser.input_args()
    try:
        connection = pymysql.connect(host,
                                     user,
                                     password,
                                     db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        if args.debug == True:
            print("Successfuly connected to", db, "database")
        return(connection)
    except pymysql.err.OperationalError:
        print("Unable to make a connection to the", db, "database, invalid credentials or server unreachable")
        return(1)

def execute_query(query, cursor, connection):
    args = argparser.input_args()
    if args.debug == True:
        print("Execute query :", query)
#    if sql_injection(query):
    try:
        cursor.execute(query)
        connection.commit()
        return(cursor)
    except:
        if args.debug == True:
            print("Unable to execute the query, check syntax or your connection to the database")
        return(1)
#    else:
#        print("Alert : sql injection attack")
        
def query_db(connection, query):
    args = argparser.input_args()
#   query="SELECT * FROM rdap;"
    try:
        cursor=connection.cursor()
        cursor=execute_query(query, cursor, connection)
        result=cursor.fetchall()
        return(result)
    except:
        if args.debug == True:
            print("Unable to execute the query")
        return(1)
#   display_result(result)
#   query="SELECT * FROM geo_ip;"
#   cursor=connection.cursor()
#   cursor=execute_query(query, cursor, connection)
#   result=cursor.fetchall()
#   print(result)

#def display_result(result):
# This function takes a dictionary as input and displays it in a prettier way than the regular print(<dict>)
#    for line in result:
#        keys=list(line.keys())
#        for i in range(len(keys)):
            #print(line[keys[0]].ljust(20), line[keys[1]].ljust(20), "\n")
#            print(keys[i]," = ", line[keys[i]], end=" | ")
#        print("\n")

def main():
    args = argparser.input_args()
    connection=connect_to_database()
    what_db=input("What table do you want to query ? (type geo_ip or rdap)\n")
    describe_table="DESCRIBE "+what_db+";"
    try:
        result=query_db(connection, describe_table)
        print(result)
    except:
        print("Could not execute the query, check the name of table")
    query=input("Type in the MySQL query (be careful to end the command with a ; which is mandatoty for MySQL syntax): \n")
    query_db(connection, query)
    connection.close()

if __name__=="__main__":
    main()
