'''Dada uma sala de dimensões NxM, localizada dentro de um museu, sendo que a 
entrada da sala esta na posição (0,0). Observe que na sala, somente existe 
uma única entrada e não existem janelas.
Na referida sala existe um quadro extremamente valioso exposto na posição (N,M), 
onde para a segurança do quadro existem Ki (i é um número não muito grande) de 
câmeras com raio de cobertura de visão Ri e com localização (Xi, Yi) na sala.

1ª Questão: Descreva um algoritmo que seja capaz de garantir o fato do valioso quadro
estar, ou não, seguro de ladrões. Comprove se o algoritmo proposto é dito ótimo.

2ª Questão: Com base na primeira parte da prova, em caso do valioso quadro não estar seguro 
da ação de ladrões, descreva um algoritmo para se obter a melhor trajetória que 
o ladrão poderá fazer para efetuar o roubo do quadro. Comprove se o algoritmo proposto é dito ótimo.'''


from collections import deque

def isSafe(N, M, cameras):
    #cameras: lista de tuplas (x, y, r) representando posição e raio de cobertura

    sala = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    # Marca áreas cobertas pelas câmeras
    for x, y, r in cameras:
        for i in range(max(0, x - r), min(N, x + r) + 1):
            for j in range(max(0, y - r), min(M, y + r) + 1):
                if (i - x)**2 + (j - y)**2 <= r**2:
                    sala[i][j] = 1  # Visível

    # Se o quadro está visível, ele está seguro
    return sala[N][M] == 1

def bestPath(N, M, cameras):
    sala = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for x, y, r in cameras:
        for i in range(max(0, x - r), min(N, x + r) + 1):
            for j in range(max(0, y - r), min(M, y + r) + 1):
                if (i - x)**2 + (j - y)**2 <= r**2:
                    sala[i][j] = 1

    # BFS para achar menor caminho não visível
    fila = deque()
    fila.append((0, 0, []))
    visitado = set()
    visitado.add((0, 0))

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while fila:
        x, y, caminho = fila.popleft()
        caminho = caminho + [(x, y)]

        if (x, y) == (N, M):
            return caminho  # Caminho mais curto

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N and 0 <= ny <= M and (nx, ny) not in visitado:
                if sala[nx][ny] == 0:
                    visitado.add((nx, ny))
                    fila.append((nx, ny, caminho))

    return None  # Não há caminho seguro










N, M = 12, 6
cameras = [(2, 3, 2), (5, 2, 1)]  # cada tupla é (x, y, raio)

if isSafe(N, M, cameras):
    print("O quadro está seguro.")
else:
    print("O quadro NAO está seguro.")
    caminho = bestPath(N, M, cameras)
    if caminho:
        print("Melhor caminho do ladrão:", caminho)
    else:
        print("Nenhum caminho seguro até o quadro.")

print("Complexidade: O(n*m) Estrutura: Fila e Matriz")