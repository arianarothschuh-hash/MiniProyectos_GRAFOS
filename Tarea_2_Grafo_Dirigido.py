def tiene_ciclo_dirigido(self):
        """Retorna True si el grafo dirigido contiene al menos un ciclo."""
        visitados = set()
        en_recursion = set()

        def dfs_ciclo(v):
            visitados.add(v)
            en_recursion.add(v)

            for vecino in self.vecinos(v):
                if vecino not in visitados:
                    if dfs_ciclo(vecino):
                        return True
                elif vecino in en_recursion:
                    return True

            en_recursion.remove(v)
            return False

        for nodo in self.adj:
            if nodo not in visitados:
                if dfs_ciclo(nodo):
                    return True
        return False