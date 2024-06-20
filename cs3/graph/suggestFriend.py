lstUser = [
    {
        "id": 1,
        "name": "Ronaldo"
    },
    {
        "id": 2,
        "name": "messi"
    },
    {
        "id": 3,
        "name": "mp3"
    },
    {
        "id": 4,
        "name": "yasuo"
    },
    {
        "id": 5,
        "name": "Duy"
    },
    {
        "id": 6,
        "name": "An"
    }
]


class Graph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex1, vertex2):

        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]

    def getNeighbor(self, vertex):
        return self.graph[vertex]

    def getGraph(self):
        print(str(self.graph))

    def getSuggest(self, vertex):
        lstNeighbor = self.getNeighbor(vertex)
        lstSuggest = set()
        for neighbor in lstNeighbor:
            lstSuggest.update(self.getNeighbor(neighbor))

        # lstSuggest = [id for id in lstSuggest if id!=vertex]
        lstSuggest.discard(vertex)
        return lstSuggest

graph = Graph()
graph.addVertex(1, 2)
graph.addVertex(1, 3)
graph.addVertex(2, 4)
graph.addVertex(3, 5)
graph.addVertex(3, 6)

for item in graph.getSuggest(2):
    uu = [user  for user in lstUser if user["id"] == item]

    for user in lstUser:
        if user["id"] == item:
            uu.append(user)

    print(uu[0])

# 1: 2, 3
# 2: 4
# 3: 5, 6

# {
#  1: [2,3]
#  2: [1,4]
#  3: [1,5,6]
#  4: [2]
#  5: [3]
#  6: [3]
# }
