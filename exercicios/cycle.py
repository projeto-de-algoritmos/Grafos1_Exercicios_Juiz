from collections import defaultdict, deque

class Solution:
    def findShortestCycle(self, n, edges):
        # Gera um grafo por lista de adjacencia
        graph = defaultdict(set)
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        # Define o tamanho do menor ciclo como um valor fora do intervalo
        min_cycle = 1001
        
        # Para todos os nos do grafo...
        for i in range(n):
            # Gera um vetor para marcar os nos visitados e seus respectivos niveis, alem da fila pra bfs
            visited = [-1] * n
            queue = [i]
            visited[i] = 0
            # Enquanto a fila nao esta vazia...
            while(queue):
                # Retira u da fila e verifica seus vizinhos v
                u = queue.pop(0)
                for v in graph[u]:
                    # Se v nao foi visitado, adiciona ele na fila e define seu nivel como o nivel de u + 1
                    if visited[v] == -1:
                        queue.append(v)
                        visited[v] = visited[u] + 1
                    # Se v ja foi visitado, verifica se ele nao eh o no de origem e se o nivel dele eh maior ou igual ao nivel de u
                    elif v != i and visited[v] >= visited[u]:
                        min_cycle = min(min_cycle, visited[u] + visited[v] + 1)

        return -1 if min_cycle == 1001 else min_cycle
  

# Para rodar no juiz online copie somente o codigo acima desse comentario
s = Solution()
print(s.findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))
print(s.findShortestCycle(n = 4, edges = [[0,1],[0,2]]))
 