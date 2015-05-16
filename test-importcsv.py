# -*- coding: utf-8 -*-
'''
test import csv
'''
import csv
import datetime
from py2neo import authenticate, Node, Relationship, Graph

authenticate('219.224.135.126:7474', 'neo4j', 'neo4j')
graph = Graph('http://219.224.135.126:7474/db/data')
csv_file_path = '/home/ubuntu5/hxq/export_test.csv'

def import_csv():
    csvfile = open(csv_file_path, 'rb')
    reader = csv.reader(csvfile)
    c_string = "LOAD CSV FROM 'file:///home/ubuntu5/hxq/export_test.csv' AS line CREATE (:test3 {name:line[0]})-[r:tweete3]->(:test3 {name:line[1]}) RETURN line"
    start_time = datetime.datetime.now()
    graph.cypher.execute(c_string)
    csvfile.close()
    end_time = datetime.datetime.now()
    interval = (end_time - start_time).seconds
    print 'interval:', interval

if __name__=='__main__':
    import_csv()
