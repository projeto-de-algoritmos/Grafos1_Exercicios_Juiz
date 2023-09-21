class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        # Verifica o numero de linhas e colunas da matriz
        m = len(image)
        n =  len(image[0])

        # Verifica qual a cor atual do ponto de inicio
        startingColor = image[sr][sc]
       
        def dfs(image, sr, sc, color):

            # Troca a cor do ponto atual
            image[sr][sc] = color

            # Define os indices dos pontos adjacentes nas 4 direcoes e marca o ponto atual como visitado
            left, up, right, down = sc - 1, sr - 1, sc + 1, sr + 1
            visited[sr][sc] = 1

            # Verifica se os pontos adjacentes estao dentro dos limite da matriz, se eles nao foram visitados
            # e se eles tem a mesma cor que o ponto de inicio tinha no comeco, caso positivo chama a dfs recursivamente
            if left >= 0 and image[sr][left] == startingColor and visited[sr][left] != 1:
                dfs(image, sr, left, color)
            if up >= 0 and image[up][sc] == startingColor and visited[up][sc] != 1:
                dfs(image, up, sc, color)
            if right < n and image[sr][right] == startingColor and visited[sr][right] != 1:
                dfs(image, sr, right, color)
            if down < m and image[down][sc] == startingColor and visited[down][sc] != 1:
                dfs(image, down, sc, color)

        # Cria uma copia da matriz para controlar quais pontos foram visitados e chama a dfs pro primeiro ponto
        visited = [[0 for col in image[0]] for line in image] 
        dfs(image, sr, sc, color)
     
        return image    
  
   
# Para rodar no juiz online copie somente o codigo acima desse comentario
s = Solution()
print(s.floodFill(image = [[1,1,1], [1,1,0], [1,0,1]], sr = 1, sc = 1, color = 2))
print(s.floodFill(image = [[0,0,0], [0,0,0]], sr = 0, sc = 0, color = 0))
 