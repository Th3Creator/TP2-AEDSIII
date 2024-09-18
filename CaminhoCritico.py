import time 
from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]
    
    def Dijkstra(self, raiz, objetivo):
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

    def DistanciaMininima(self, dist, sptSet):
        min_dis = sys.maxsize
        min_index = 0
        for u in range(self.V):
            if dist[u] < min_dis and sptSet[u] == False:
                min_dis = dist[u]
                min_index = u
        return min_index

    def DistanciaMaxima():
        return "hw"

def LeArquivoCSV(caminho):
    print("hw")

def Menu():
    while True:  
        print("\n\n")
             
        escolha = input("Escolha uma opção: ")

        grafo = Grafo(numeroDeElementos)

        if escolha == '1':
           
            print(f"hw")
        else:
            print("Opção inválida. Tente novamente.")

Menu()  


"""
IMPLEMENTAÇÃO:


# Faz com que leia um arquivo .csv, e faça a separação por meio do caractere especial "," e imprima
LeArquivoCSV():




"""