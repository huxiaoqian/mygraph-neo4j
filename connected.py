# -*- coding: utf-8 -*-
from py2neo import authenticate, Graph, Node, Relationship
'''
host_port:"localhost：7474"
user_name:"neo4j"
password:"123456"
'''
authenticate("localhost:7474", "neo4j", "123456")
graph = Graph("http://localhost:7474/db/graph1/")

alice = Node("Person", name="Alice", age="10")
dan = Node("Person", name="Dan", age="23")
a2d = Relationship(alice, "KNOWS", dan)
graph.create(alice)
graph.create(dan)
graph.create(a2d)
print "graph uri:", graph
print "graph resource:", graph.resource
print "graph node num:", graph.order
print "graph node alice:", graph.node(0)
print "graph relation size:", graph.size


