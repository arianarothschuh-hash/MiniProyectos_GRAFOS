def dfs_iterativo(self, inicio):
        """Recorrido en Profundidad (Iterativo)."""
        visitados = set()
        pila = [inicio]
        resultado = []

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)

                # Agregamos los vecinos en orden inverso (opcional) 
                # para mantener un orden similar al DFS recursivo
                for vecino in reversed(self.vecinos(actual)):
                    if vecino not in visitados:
                        pila.append(vecino)
                        
        return resultado