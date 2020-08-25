class Vertex:
    def __init__(self, data):
        self.data = data
        self.edges = {}


    def add_edge(self, data, weight):
        self.edges[data] = weight

    def get_edges(self):
        return self.edges.keys()


class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, vertex):
        self.vertices[vertex.data] = vertex


    def add_edge(self, vertex_a, vertex_b, price, time):
        self.vertices[vertex_a.data].add_edge(vertex_b.data, {"price": price, "time": time})
        if not self.directed:
            self.vertices[vertex_b.data].add_edge(vertex_a.data, {"price": price, "time": time})



travel = Graph(directed=False)
cities = [
Vertex("Kuwait"), Vertex("Dubai"), Vertex("Colombo"),
 Vertex("Male"), Vertex("Doha"), Vertex("Tokyo"), Vertex("Oslo")
]

for city in cities:
    travel.add_vertex(city)

travel.add_edge(cities[0], cities[1], 120, 2)
travel.add_edge(cities[0], cities[2], 200, 4)
travel.add_edge(cities[2], cities[2], 60, 1)
travel.add_edge(cities[1], cities[4], 100, 1.5)
travel.add_edge(cities[4], cities[5], 500, 11)
travel.add_edge(cities[1], cities[6], 300, 6)

for city in travel.vertices.keys():
    print(f"- {city}")

from_city = input("from: ")

for x in travel.vertices[from_city].get_edges():
    print(f"- {x}")

to_city = input("to: ")

print(travel.vertices[from_city].edges[to_city])
