from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.parents = {}

    def add_edge(self, source, destination):
        self.parents[source] = None
        self.parents[destination] = None
        self.graph[source].append(destination)

    def set_parent(self, x, y):
        self.parents[x] = y

    def find_until_no_parent(self, vertex):
        if self.parents[vertex] is None:
            return vertex

        return self.find_until_no_parent(self.parents[vertex])

    def is_cyclic(self):
        for i in self.graph:
            for j in self.graph[i]:
                s = self.find_until_no_parent(i)
                d = self.find_until_no_parent(j)

                if s == d:
                    return True

                self.set_parent(s, d)


def union_find():
    g = Graph()
    g.add_edge("a", "b")
    g.add_edge("b", "c")
    g.add_edge("c", "d")
    g.add_edge("d", "e")
    g.add_edge("e", "f")
    g.add_edge("a", "f")

    if g.is_cyclic():
        print("Graph contains cycle")
    else:
        print("Graph does not contain cycle")
