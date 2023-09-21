from collections import defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        # Constroi um grafo bipartido com arestas entre as paradas e os respectivos onibus que passam nelas
        graph = defaultdict(set)
        for bus, stops in enumerate(routes):
            for stop in stops:
                graph[stop].add(bus)

        # Define dois conjuntos de vertices visitados, um para as paradas e outro para os onibus
        visitedBus = set()
        visitedStop = set()
        # Define uma fila com a parada de inicio e quantos onibus para chegar ate ela(0)
        queue = [(source, 0)]        

        # Enquanto a fila nao esta vazia...
        while queue:
            # Remove um vertice da fila, se ele for a parada de destino retorna o numero de onibus necessario
            vertex, busesNum = queue.pop(0)
            if vertex == target:
                return busesNum
            # Verifica no grafo todos os onibus que passam naquela parada
            for bus in graph[vertex]:
                # Se esse onibus nao foi visitado, adiciona ele no conjunto de visitados
                if bus not in visitedBus:
                    visitedBus.add(bus)
                    # Verifica todas as paradas em que esse onibus passa
                    for stop in routes[bus]:
                        # Se a parada ainda nao foi visitada, adiciona ela as visitadas
                        if stop not in visitedStop:
                            visitedStop.add(stop)
                            # Adiciona a parada na fila e incrementa o numero de onibus necessarios para chegar nela
                            queue.append((stop, busesNum + 1))   
        return -1


# Para rodar no juiz online copie somente o codigo acima desse comentario
s = Solution()
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))
print(s.numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 2))
 