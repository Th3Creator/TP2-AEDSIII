# dijkstra: https://github.com/HenriqueNizolli/Algoritmo_de_Dijkstra
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]

    def print_solution(self, dist):
        print("Vértice | Distância da Origem")
        for i in range(self.V):
            print(i, "\t|\t", dist[i])

    def min_distance(self, dist, sptSet):
        min_dis = sys.maxsize
        min_index = 0
        for u in range(self.V):
            if dist[u] < min_dis and sptSet[u] == False:
                min_dis = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, raiz, objetivo):
        caminho = []
        dist = [sys.maxsize] * self.V
        dist[raiz] = 0
        spt_set = [False] * self.V
        for cout in range(self.V):
            x = self.min_distance(dist, spt_set)
            spt_set[x] = True
            for y in range(self.V):
                if self.graph[x][y] > 0 and spt_set[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    caminho.append([x, y, dist[y]])
        self.print_solution(dist)
        caminho.reverse()
        self.caminho(caminho, raiz,objetivo)

    def caminho(self, caminho, raiz, objetivo):
        aux = []
        origem = -1
        while not origem == raiz:
            for i in range(len(caminho)):
                if caminho[i][1] == objetivo:
                    aux.append(caminho[i])
                    objetivo = caminho[i][0]
                    origem = caminho[i][0]
        aux.reverse()
        print("\n movimento|\tvertive inicial|\tvertice final|\tdistancia")
        for i in range(len(aux)):
            print(i, "\t \t |\t \t", aux[i][0], "\t\t\t|\t", aux[i][1], "\t\t\t|\t", aux[i][2])
        print("\n   sequencia     |   distancia total")
        sequencia = []
        for i in range(len(aux)):
            if i == (len(aux)-1):
                sequencia.append(aux[i][0])
                sequencia.append(aux[i][1])
            else:
                sequencia.append(aux[i][0])
        print(sequencia, " |\t   ", aux[(len(aux)-1)][2])

g = Graph(5)

# Matriz de Custo
g.graph = [[0, 2, 7, 0, 0],
           [0, 0, 2, 8, 5],
           [0, 3, 0, 1, 0],
           [0, 0, 0, 0, 4],
           [0, 0, 0, 5, 0]
           ]

# indicar qual sera o vertice raiz e o vertice que deseja chegar
g.dijkstra(0, 4)