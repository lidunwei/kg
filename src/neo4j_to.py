from py2neo import Graph, Node, Relationship
from config import Config
import json


def get_data(type_n, name):
    neo4j_graph = Graph(Config.GRAPH_HOST, user=Config.GRAPH_USER, password=Config.GRAPH_PASSWD)
    expr = 'MATCH p=(n:' + type_n + '{name:"' + name + '"})-[]->(m) RETURN p'
    a = neo4j_graph.run(expr).data()
    result = []
    relation = []
    for i in range(len(a)):
        start_node = a[i]['p'].start_node['name']
        end_node = a[i]['p'].end_node['name']
        relationships = a[i]['p'].relationships
        for j in range(len(relationships)):
            relationship = type(relationships[j]).__name__
            if dict(relationships[j]):
                relationship = {relationship: dict(relationships[j])}
            result.append([start_node, end_node, relationship])
            if relationship not in relation:
                relation.append(relationship)
    result_list = {}
    for element in relation:
        if isinstance(element, dict):
            key = [key for key, value in element.items()][0]
            result_list[key] = []
            for children in result:
                if isinstance(children[2], dict):
                    if [key for key, value in children[2].items()][0] == key:
                        print(children)
                        result_list[key].append([value for key, value in children[2].items()][0])
        else:
            result_list[element] = []
            for children in result:
                if children[2] == element:
                    result_list[element].append(children[1])
    final_result = {}
    for key, value in result_list.items():
        key = key.replace("对应", "")
        if len(value) == 1:
            final_result[key] = value[0]
        else:
            final_result[key] = value
    return final_result


name_g = "袁天罡"
type_n_g = "人物名称"
print(get_data(type_n_g, name_g))
