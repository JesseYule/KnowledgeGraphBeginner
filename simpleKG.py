from py2neo import Graph, Node, Relationship

# 连接Neo4j
g = Graph(
    host='127.0.0.1',
    http_port=7474,
    user='neo4j',
    password='neo4j')

# 创建节点
da_vinci = Node('person', name='DA VINCI')
mona_lisa = Node('art', name='MONA LISA')
louvre = Node('place', name='LOUVRE')

g.create(da_vinci)
g.create(mona_lisa)
g.create(louvre)

relation1 = Relationship(da_vinci, 'painted', mona_lisa)
relation2 = Relationship(mona_lisa, 'is_in', louvre)

g.create(relation1)
g.create(relation2)





