# -*- coding: utf-8 -*-
from py2neo import authenticate, Graph, Node, Relationship
'''
host_port:"localhost：7474"
user_name:"neo4j"
password:"123456"
'''
authenticate("219.224.135.126:7474", "neo4j", "neo4j")
graph = Graph("http://219.224.135.126:7474/db/data/")
'''
alice = Node("test1", name="Alice2", age="10")
dan = Node("test1", name="Dan2", age="23")
a2d = Relationship(alice, "KNOWS", dan)
graph.create(alice)
graph.create(dan)
graph.create(a2d)
print "graph uri:", graph
print "graph resource:", graph.resource
print "graph node num:", graph.order
print "graph node alice:", graph.node(0)
print "graph relation size:", graph.size
'''
c_string = "LOAD CSV FROM 'file:///home/ubuntu5/hxq/import-test.csv' AS line CREATE (:test {name:line[1], year:line[2]}) return line"
graph.cypher.execute(c_string)

