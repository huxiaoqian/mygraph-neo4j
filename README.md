# mygraph-neo4j
use Neo4j and py2neo to construct graph

##1 neo4j安装
```
neo4j 官网下载  neo4j-community-2.2.1-unix.tar.gz(社区版-不支持集群)
tar -zvxf neo4j-community-2.2.1-unix.tar.gz
进入安装解压后的文件夹 ./bin/neo4j start
```
database 位置在本地：/home/neo4j/neo4j-community-2.2.1/data/graph.db

开启页面webadmin  打开页面http://localhost:7474/webadmin
username: neo4j
password: 123456

页面服务：
Dashboard / 可视化数据库增减变化
Data browser/ 迭代查询节点可视化网络结构
Console / neo4j的shell
Indexes / 索引管理

本地服务器开启shell命令行：
```
进入路径：
   /home/neo4j/neo4j-community-2.2.1
开启本地db对应的shell命令行
   ./bin/neo4j-shell -path home/ubuntu5/neo4j/neo4j-community-2.2.1/db/data
进入后 neo4j-sh (?)$
```


##2 py2neo安装
```
 pip install py2neo
```
官网 py2neo.org/2.0/

