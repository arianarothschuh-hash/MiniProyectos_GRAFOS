# Unidad 10: Grafos

## 1. Objetivos de Aprendizaje
Al finalizar esta unidad, los estudiantes serán capaces de:
- Comprender los conceptos fundamentales de la teoría de grafos.
- Diferenciar entre grafos dirigidos/no dirigidos y ponderados/no ponderados.
- Implementar grafos utilizando matrices y listas de adyacencia.
- Ejecutar y comprender algoritmos de recorrido: Búsqueda en Anchura (BFS) y Búsqueda en Profundidad (DFS).
- Aplicar el algoritmo de Dijkstra para encontrar el camino más corto.

## 2. Conceptos Teóricos

### Definición Básica
Un grafo es una estructura de datos no lineal que consta de:
- **Vértices (Nodos):** Entidades o puntos de datos.
- **Aristas (Edges):** Conexiones o enlaces entre los vértices.

**Analogía del Mundo Real:** Imagina un mapa de aerolíneas. Los aeropuertos son los vértices y las rutas de vuelo entre ellos son las aristas.

### Tipos de Grafos
- **Dirigidos vs No Dirigidos:** En un grafo dirigido, las aristas tienen una dirección específica (como calles de un solo sentido). En los no dirigidos, la conexión es bidireccional (como una videollamada entre dos personas).
- **Ponderados vs No Ponderados:** En un grafo ponderado, cada arista tiene un peso o costo asociado (por ejemplo, distancia o peaje).
- **Conexos:** Existe un camino entre cualquier par de vértices.
- **Cíclicos vs Acíclicos:** Los cíclicos contienen al menos un ciclo (un camino que empieza y termina en el mismo vértice). Los acíclicos no.

### Representaciones

#### Matriz de Adyacencia
Una matriz 2D de tamaño V x V donde V es el número de vértices.
- `Matriz[i][j] = 1` si hay arista entre i y j.
- Ocupa mucho espacio: O(V²).

```ascii
Grafo: A --- B
       |     |
       C --- D

Matriz de Adyacencia:
  A B C D
A 0 1 1 0
B 1 0 0 1
C 1 0 0 1
D 0 1 1 0
```

#### Lista de Adyacencia
Un arreglo o diccionario de listas. Cada vértice tiene una lista de sus vecinos.
- Eficiente en espacio para grafos dispersos: O(V + E).

```ascii
Lista de Adyacencia:
A: [B, C]
B: [A, D]
C: [A, D]
D: [B, C]
```

### Grado de un Vértice
El número de aristas conectadas a un vértice. En grafos dirigidos se divide en grado de entrada (in-degree) y de salida (out-degree).

### Recorridos
- **BFS (Búsqueda en Anchura):** Explora nivel por nivel usando una Cola (Queue).
- **DFS (Búsqueda en Profundidad):** Explora lo más profundo posible antes de retroceder, usando una Pila (Stack) o recursividad.

## 3. Implementación en Python

```python
from collections import deque

class Grafo:
    def __init__(self, dirigido=False):
        """Inicializa un grafo con una lista de adyacencia (diccionario)."""
        self.adj = {}
        self.dirigido = dirigido

    def agregar_vertice(self, v):
        """Agrega un vértice al grafo."""
        if v not in self.adj:
            self.adj[v] = []

    def agregar_arista(self, u, v):
        """Agrega una arista entre u y v."""
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        self.adj[u].append(v)
        if not self.dirigido:
            self.adj[v].append(u)

    def vecinos(self, v):
        """Retorna los vecinos de un vértice."""
        return self.adj.get(v, [])

    def bfs(self, inicio):
        """Recorrido en Anchura."""
        visitados = set()
        cola = deque([inicio])
        resultado = []

        visitados.add(inicio)

        while cola:
            actual = cola.popleft()
            resultado.append(actual)

            for vecino in self.vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
                    
        return resultado

    def dfs(self, inicio, visitados=None, resultado=None):
        """Recorrido en Profundidad (Recursivo)."""
        if visitados is None:
            visitados = set()
            resultado = []

        visitados.add(inicio)
        resultado.append(inicio)

        for vecino in self.vecinos(inicio):
            if vecino not in visitados:
                self.dfs(vecino, visitados, resultado)
                
        return resultado

    def mostrar(self):
        """Muestra el grafo."""
        for v, vecinos in self.adj.items():
            print(f"{v} -> {vecinos}")


class GrafoPonderado(Grafo):
    def __init__(self, dirigido=False):
        super().__init__(dirigido)
        # adj será un dict donde la clave es el vértice y el valor es una lista de tuplas (vecino, peso)

    def agregar_arista(self, u, v, peso):
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        self.adj[u].append((v, peso))
        if not self.dirigido:
            self.adj[v].append((u, peso))
            
    def vecinos(self, v):
        """Retorna los vecinos de un vértice sin el peso para compatibilidad."""
        return [vecino for vecino, peso in self.adj.get(v, [])]
        
    def dijkstra(self, inicio):
        """
        Calcula el camino más corto desde 'inicio' a todos los demás vértices.
        """
        import heapq
        distancias = {v: float('infinity') for v in self.adj}
        distancias[inicio] = 0
        pq = [(0, inicio)] # (distancia, vertice)
        
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
```

## 4. Ejemplos Resueltos

### Ejemplo 1: Mapa de Ciudades (No dirigido)
```python
g = Grafo()
g.agregar_arista('Madrid', 'Barcelona')
g.agregar_arista('Madrid', 'Valencia')
g.agregar_arista('Barcelona', 'Zaragoza')
g.mostrar()
```

### Ejemplo 2: Red Social (Dirigido)
```python
g = Grafo(dirigido=True)
g.agregar_arista('Alice', 'Bob') # Alice sigue a Bob
g.agregar_arista('Alice', 'Charlie')
g.agregar_arista('Bob', 'Alice')
```

### Ejemplo 3: BFS para encontrar conectados
```python
g = Grafo()
# ... agregar aristas ...
print("Orden BFS:", g.bfs('Alice'))
```

### Ejemplo 4: Dijkstra para Ruta Mínima
```python
gp = GrafoPonderado()
gp.agregar_arista('A', 'B', 4)
gp.agregar_arista('A', 'C', 2)
gp.agregar_arista('C', 'B', 1)
gp.agregar_arista('B', 'D', 5)
print("Distancias mínimas desde A:", gp.dijkstra('A'))
```

## 5. Práctica en Clase
1. Crea un grafo que represente un árbol genealógico.
2. Implementa un método `es_conexo()` que use BFS.
3. Encuentra la ruta más corta (en saltos) usando BFS.
4. Simula un sistema de vuelos con costos y usa Dijkstra para viajar económico.

## 6. Tarea / Homework
1. Escribir un método iterativo para DFS.
2. Implementar un método para detectar si hay ciclos en un grafo dirigido.
3. Crear un grafo ponderado que represente una red de tráfico de red y encontrar el camino de menor latencia.
4. Implementar un método que retorne el camino exacto (lista de nodos) tras ejecutar Dijkstra, no solo la distancia.
5. Calcular el grado de entrada y salida de cada nodo en un grafo dirigido.

## 7. Mini-Proyecto: Sistema de Navegación GPS

**Enunciado:**
Construye un sistema que modela ciudades y autopistas. Cada ciudad es un nodo y cada autopista es una arista ponderada por el tiempo en minutos. El usuario debe poder ver todas las ciudades, agregar nuevas rutas, y consultar la ruta más rápida entre dos ciudades especificando el recorrido completo.

**Rúbrica:**
- Implementación de Grafo Ponderado (25%)
- Algoritmo Dijkstra con reconstrucción de ruta (35%)
- Interfaz de usuario (Consola) (20%)
- Manejo de excepciones y casos límite (10%)
- Calidad de código y comentarios (10%)
