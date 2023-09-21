class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order = []
        # Calcula o grau de entrada de todos os vertices do grafo e armazena no vetor enterDeg
        enterDeg = [0 for _ in range(numCourses)]
        for edge in range(len(prerequisites)):
            enterDeg[prerequisites[edge][0]] += 1  
        # Inicializa uma fila somente com os vertices com grau de entrada igual a 0
        queue = [v for v in range(numCourses) if enterDeg[v] == 0]

        # Enquanto ainda existem vertices com grau de entrada igual a 0...
        while queue:
            # Remove o vertice da fila e adiciona no vetor da ordem topologica
            vertex = queue.pop()
            order.append(vertex)
            # Remove o vertice do grafo e atualiza o grau de entrada de seus vizinhos
            for edge in range(len(prerequisites)):
                neighbour = prerequisites[edge][0]
                if prerequisites[edge][1] == vertex:
                    enterDeg[neighbour] -= 1
                    # Se  o grau de entrada de algum vizinho virar 0 ele entra na fila
                    if enterDeg[neighbour] == 0:
                        queue.append(neighbour)
        # Se ainda ha algum vertice com grau de entrada diferente de 0 entao nao existe ordenacao topologica desse grafo                                
        for v in enterDeg:
            if v != 0: return []

        return order


# Para rodar no juiz online copie somente o codigo acima desse comentario
s = Solution()
print(s.findOrder(2, [[1, 0]]))
print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(s.findOrder(1, []))
