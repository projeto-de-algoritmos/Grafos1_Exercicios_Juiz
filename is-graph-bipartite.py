class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def bfs(graph):
            # Visita todos os nos do grafo
            for v in range(len(graph)):
                # Se o no nao foi visitado, adiciona na fila e define a "cor" dele como 1
                if visited[v] == 0:
                    queue.append(v)
                    visited[v] = 1
                    # Enquanto a fila nao esta vazia...
                    while(queue):
                        # Retira u da fila e verifica seus vizinhos v
                        u = queue.pop(0)
                        for v in graph[u]:
                            # Se v nao foi visitado, adiciona ele na fila e define a "cor" dele como a cor inversa de u
                            if visited[v] == 0:
                                queue.append(v)
                                visited[v] = 2 if visited[u] == 1 else 1
                            # Se v ja foi visitado, verifica se sua cor eh igual a do seu vizinho u, se sim o grafo nao e bipartido
                            elif visited[v] == visited[u]:
                                return False
            return True
        
        # Define o vetor de visitados e a fila
        visited = [0 for vertex in graph]
        queue = []

        return bfs(graph)


# Para rodar no juiz online copie somente o codigo acima desse comentario
s = Solution()
print(s.isBipartite(graph = [[1,2,3],[0,2],[0,1,3],[0,2]]))
print(s.isBipartite(graph = [[1,3],[0,2],[1,3],[0,2]]))

