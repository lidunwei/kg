import json

from py2neo import Graph, Node

from config import Config



class toNeo:
    def __init__(self):
        self.neo4j_graph = Graph(Config.GRAPH_HOST, user=Config.GRAPH_USER, password=Config.GRAPH_PASSWD)

    def create_relation_ship(self, start_node, end_node, edges, rel_name):
        """
        创建实体关系边
        :param start_node:
        :param end_node:
        :param edges:
        :param rel_name:
        :return:
        """
        try:
            count = 0
            # 去重处理
            set_edges = []
            for edge in edges:
                set_edges.append('###'.join(edge))
            for edge in set(set_edges):
                edge = edge.split('###')
                p = edge[0]
                q = edge[1]
                query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s]->(q)" % (
                    start_node, end_node, p, q, rel_name)
                print(query)
                try:
                    self.neo4j_graph.run(query)
                    count += 1
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
            pass
        return

    def query_node(self, label, name):
        """
        查询节点是否存在
        :param label: 节点label
        :param name: 节点名字
        :return: 0不存在，1存在
        """
        sql = 'Match (n:%s) where n.name = "%s" return n' % (label, name)
        result = self.neo4j_graph.run(sql).data()
        if len(result) == 0:
            return 0
        else:
            return 1

    def create_node(self, label, name):
        """
        创建节点
        :param label: 节点标签
        :param name: 节点
        :return:
        """
        node = Node(label, name=name)
        self.neo4j_graph.create(node)

    def relat_exists(self, label, node1, node2, relat):
        """"
        判断关系是否存在
        """
        global rel
        query = "match p=(:%s{name:'%s'})-[]-(m) where m.name='%s' return p" % (label, node1, node2)
        try:
            result = self.neo4j_graph.run(query).data()
            rel = []
            for i in result:
                for j in i['p'].relationships:
                    rel.append(type(j).__name__)
        except Exception as e:
            result = []
            print(e)
        if len(result) != 0 and relat in rel:
            return False
        else:
            return True
    def data_to_neo4j(self,data):
        for key,value in data.items():
            if self.query_node("人物名称", name=key) == 0:
                self.create_node("人物名称", key)
            for key_,value_ in value.items():
                print(key_)
                if isinstance(value_, list):
                    for element in value_:
                        if self.query_node(key_, name=element) == 0:
                            self.create_node(key_, element)
                        status = self.relat_exists("人物名称", key, element, "对应"+key_)
                        if status:
                            self.create_relation_ship("人物名称", key_, [[key, element]], "对应"+key_)
                else:
                    if self.query_node(key_, name=value_) == 0:
                        self.create_node(key_, value_)
                    status = self.relat_exists("人物名称", key, value_, "对应" + key_)
                    if status:
                        self.create_relation_ship("人物名称", key_, [[key, value_]], "对应" + key_)


if __name__ == '__main__':
    data ={
      "袁天罡": {
        "身份": [
          "大唐国师",
          "不良帅",
          "天魁星"
        ],"别称": "大帅",
        "出生年代": "唐太宗年间",
        "成就": "建立不良人",
        "好友": "李淳风",
        "手下": [
          "阳叔子",
          "陆佑劫",
          "慧明",
          "上官云阙",
          "温韬",
          "蚩笠",
          "蚩离",
          "镜心魔",
          "孟婆"
        ],
        "人物特点": [
          "对李唐王室忠心耿耿",
          "星象占扑造诣高深",
          "武力通玄，无上境界之上",
          "长生不老",
          "容貌尽毁",
          "好于女色",
          "冷酷无情"
        ],
        "武器": "华阳针",
        "武功": [
          "华阳针法",
          "天罡诀",
          "缚灵阵"
        ],
        "内力": "集所有人之力也无法战胜的恐怖存在",
        "历史原型": [
          "星象学家",
          "相士",
          "道士"
        ],
        "居住地": "终南山藏兵谷",
        "所属": "唐",
        "门派": "不良人",
        "徒弟": "李星云"
      }
    }
    toNeo().data_to_neo4j(data)
