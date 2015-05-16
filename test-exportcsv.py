# -*- coding: utf-8 -*-
'''
test export data from neo4j to csv
'''
import csv
import datetime
from py2neo import authenticate, Node, Relationship, Graph

authenticate('219.224.135.126:7474', 'neo4j', 'neo4j')
graph = Graph('http://219.224.135.126:7474/db/data')
csv_file = '/home/ubuntu5/hxq/export_test.csv'

def export_csv():
    csvfile = open(csv_file, 'wb')
    writer = csv.writer(csvfile)
    query_string = 'MATCH (a:test2)-[retweete]-(b:test2) RETURN a.name, b.name ORDER BY a.name'
    start_time = datetime.datetime.now()
    for record in graph.cypher.stream(query_string):
        #print 'record:', record
        writer.writerow([record[0], record[1]])
    end_time = datetime.datetime.now()
    interval = (end_time - start_time).seconds
    print 'interval:', interval
    csvfile.close()

if __name__=='__main__':
    export_csv()
