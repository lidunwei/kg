import json

all_nodes = []
with open("data.json", encoding="utf8") as f:
    data = json.load(f)["data"]
    count = 0
    for temp in data:
        for key, value in temp.items():
            nodes = [{
                "name": key,
                "role_id": count,
                "group": 1,
                "avatar": "./img/140646844806.jpg"
            }]
            count = count + 1
            for key_, value_ in value.items():
                if isinstance(value_, list):
                    nodes.append({
                        "name": key_,
                        "role_id": count,
                        "group": 2,
                        "avatar": "./img/140646844806.jpg"
                    })
                    count = count + 1
                    for element in value_:
                        nodes.append({
                            "name": element,
                            "role_id": count,
                            "group": 2,
                            "avatar": "./img/140646844806.jpg"
                        })
                        count = count + 1
                else:
                    nodes.append({
                        "name": value_,
                        "role_id": count,
                        "group": 2,
                        "avatar": "./img/140646844806.jpg"
                    })
                    count = count + 1
            all_nodes.append(nodes)
all_links = []
for temp in data:
    count = 0
    all_count = []
    for key, value in temp.items():
        count = count + 1
        links = []
        for key_, value_ in value.items():
            if isinstance(value_, list):
                links.append({
                    "source": 0,
                    "target": count,
                    "relation": key_,
                    "color": "887400"
                })
                count = count + 1
                all_count.append(count)
                for element in value_:
                    links.append({
                        "source": all_count[len(all_count) - 1] - 1,
                        "target": count,
                        "relation": '包含',
                        "color": "00748d"
                    })
                    count = count + 1
            else:
                links.append({
                    "source": 0,
                    "target": count,
                    "relation": key_,
                    "color": "88748d"
                })
                count = count + 1
        all_links.append(links)
all_name = []
result = {"nodes": [], "links": []}
for element in all_nodes[0]:
    result["nodes"].append(element)
for element in all_links[0]:
    result["links"].append(element)
