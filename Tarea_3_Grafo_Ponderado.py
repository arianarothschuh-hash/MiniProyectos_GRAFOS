from collections import deque
import heapq

# 1. Definición de la clase base Grafo
class Grafo:
    def __init__(self, dirigido=False):
        self.adj = {}
        self.dirigido = dirigido

    def agregar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def agregar_arista(self, u, v):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adj[u].append(v)
        if not self.dirigido:
            self.adj[v].append(u)

    def vecinos(self, v):
        return self.adj.get(v, [])

# 2. Definición de la clase GrafoPonderado (hereda de Grafo)
class GrafoPonderado(Grafo):
    def __init__(self, dirigido=False):
        super().__init__(dirigido)

    def agregar_arista(self, u, v, peso):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        self.adj[u].append((v, peso))
        if not self.dirigido:
            self.adj[v].append((u, peso))
            
    def vecinos(self, v):
        return [vecino for vecino, peso in self.adj.get(v, [])]
        
    def dijkstra(self, inicio):
        distancias = {v: float('infinity') for v in self.adj}
        distancias[inicio] = 0
        pq = [(0, inicio)]
        
        while pq:
            dist_actual, actual = heapq.heappop(pq)
            
            if dist_actual > distancias[actual]:
                continue
                
            for vecino, peso in self.adj.get(actual, []):
                distancia = dist_actual + peso
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pq, (distancia, vecino))
                    
        return distancias

# 3. Tu ejemplo de uso (ahora sí funcionará)
red = GrafoPonderado(dirigido=True)
red.agregar_arista('RouterA', 'RouterB', 12)  # 12 ms de latencia
red.agregar_arista('RouterA', 'RouterC', 5)
red.agregar_arista('RouterC', 'RouterB', 2)
red.agregar_arista('RouterB', 'RouterD', 8)
red.agregar_arista('RouterC', 'RouterD', 20)

latencias_minimas = red.dijkstra('RouterA')
print("Menor latencia desde RouterA:", latencias_minimas)