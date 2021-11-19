from collections import defaultdict


# class Node:
#     def __init__(self, name, data):
#         self.name = name
#         self.data = data
#
#
# class Edge:
#     def __init__(self, source, destination, weight):
#         self.source = source
#         self.destination = destination
#         self.weight = weight


class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.graph = []
        self.rank_mapping = {}

    def add_edge(self, source, destination, weight):
        self.rank_mapping[source] = {
            "parent": -1, "rank": 0
        }
        self.rank_mapping[destination] = {
            "parent": -1, "rank": 0
        }
        self.graph.append({"source": source, "destination": destination, "weight": weight})

    def find(self, node):
        if self.rank_mapping[node]["parent"] != -1:
            self.rank_mapping[node]["parent"] = self.find(self.rank_mapping[node]["parent"])
            return self.rank_mapping[node]["parent"]
        else:
            return node

    def union(self, s, d):
        s_rank = self.rank_mapping[s]["rank"]
        d_rank = self.rank_mapping[d]["rank"]

        if s_rank > d_rank:
            self.rank_mapping[d]["parent"] = s
        elif d_rank < d_rank:
            self.rank_mapping[s]["parent"] = d
        else:
            self.rank_mapping[s]["parent"] = d
            self.rank_mapping[d]["rank"] = d_rank + 1

    def find_kruskal_mst(self):
        # Sort the graph edges based on the weight
        self.graph = sorted(self.graph, key=lambda x: x.get('weight'))
        mst_edges = []

        for edge in self.graph:
            s_node = self.find(edge["source"])
            d_node = self.find(edge["destination"])

            if s_node != d_node:
                mst_edges.append(edge)
                self.union(s_node, d_node)

        for e in mst_edges:
            print(e)


def kruskal_mst():
    graph = Graph(6, 10)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 3)
    graph.add_edge(0, 2, 2)
    graph.add_edge(1, 4, 3)
    graph.add_edge(2, 4, 1)
    graph.add_edge(2, 3, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(3, 4, 2)
    graph.add_edge(3, 5, 4)
    graph.add_edge(4, 5, 3)

    graph.find_kruskal_mst()
