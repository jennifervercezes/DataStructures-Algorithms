'''
1a Questão:
Em uma ilha existem n jesuítas e n canibais que convivem de forma pacífica 
pois habitam o mesmo número n para as duas populações (equilíbrio natural). 
Todavia, a Ilha será destruída por um tsunami 24 horas e, para evitar a morte 
da população, toda a ilha deverá ser evacuada para um determinado local no 
continente, porém somente existe um único barco com 2 lugares que leva 10 minutos em uma travessia.
Desenvolva um algoritmo capaz de simular a evacuação da ilha em um menor tempo 
possível, mas que, por medida de segurança, não deve ser permitido que em momento 
algum a quantidade de jesuítas seja inferior à de canibais (senão o canibal come 
o jesuíta), seja na ilha, no continente ou no barco.
Lembre-se que um barco não navega sozinho!

Analise a complexidade do algoritmo proposta e diga se o mesmo é dito um algoritmo ótimo. 
Lembre-se de obrigatoriamente definir a função tempo do algoritmo proposto !
Lembre-se de descrever qual a estrutura de dados que a sua proposta algoritmica utiliza!
Com base no algoritmo proposto determine qual o número p (p<=n) de canibais e jesuítas que serão realmente salvos do tsunami.


2a Questão:
Desenvolva um algoritmo que, dado as sequências de nós que descreve uma função matemática 
nas formas infixa e prefixa - os caracteres especiais "("e ")" são indicativos de 
precedência obrigatória para uma subfunção matemática, seja capaz de reconstruir a arvore 
binária para esta função matemática e a partir desta criar a sequencia de nós que descreve 
a função matemática na forma pósfixa.
Aplique o algoritmo proposto para reconstruir (faça o esquema da árvore) a árvore binária 
referente às formas infixa Z+Q* (T/L - M) e prefixa +Z Q (-/TL M). Lembre-se que os 
caracteres especiais "("e")" são indicativos de precedência obrigatória para uma subfunção 
matemática e apresente a sequencia de nós para a forma pósfixa.
Analise a complexidade do algoritmo proposto e diga se o mesmo é dito um algoritmo ótimo. 
Lembre-se de obrigatoriamente definir a função tempo do algoritmo proposto!
Lembre-se de descrever qual a estrutura de dados que a sua proposta algorítmica utiliza!'''


from collections import deque

def is_safe(j, c):
    return j == 0 or j >= c

def estado_valido(ij, ic, cj, cc):
    return is_safe(ij, ic) and is_safe(cj, cc)

def evacuar(n):
    estado_inicial = (n, n, 0, 0)  # (jesuítas, canibais, barco_na_ilha, tempo)
    visitados = set()
    fila = deque()
    fila.append((estado_inicial, []))  # estado + caminho

    melhores_salvos = 0
    melhor_tempo = float('inf')

    while fila:
        (ij, ic, barco, tempo), caminho = fila.popleft()
        cj, cc = n - ij, n - ic  # continente
        
        # Verificar estado válido
        if not estado_valido(ij, ic, cj, cc):
            continue

        if (ij, ic, barco) in visitados:
            continue
        visitados.add((ij, ic, barco))

        novo_caminho = caminho + [((ij, ic), (cj, cc), barco, tempo)]

        # Caso base: todos foram salvos
        if ij == 0 and ic == 0:
            if tempo <= 24 * 60:
                return n, tempo, novo_caminho
            continue

        # Gerar movimentos possíveis (barco leva 1 ou 2 pessoas)
        movimentos = [(1,0), (0,1), (1,1), (2,0), (0,2)]

        for mj, mc in movimentos:
            if barco == 0:  # barco está na ilha → indo pro continente
                if ij >= mj and ic >= mc:
                    new_ij = ij - mj
                    new_ic = ic - mc
                    new_estado = (new_ij, new_ic, 1, tempo + 10)
                    fila.append((new_estado, novo_caminho))
            else:  # barco está no continente → voltando
                if cj >= mj and cc >= mc:
                    new_ij = ij + mj
                    new_ic = ic + mc
                    new_estado = (new_ij, new_ic, 0, tempo + 10)
                    fila.append((new_estado, novo_caminho))

    # Nenhuma solução total possível → tentar salvar p < n
    for p in reversed(range(n)):
        # Reduzir n artificialmente e tentar
        resultado = evacuar(p)
        if resultado:
            return resultado

    return 0, 0, []

def q1():
    n = 17
    salvos, tempo, caminho = evacuar(n)

    print(f"Máximo salvo: {salvos}")
    print(f"Tempo gasto: {tempo} minutos")

    print("Etapas:")
    for est in caminho:
        print(est)

    print("Complexidade O(n²) Estrutura: Fila")














#--------------------------------------------------------------------------------
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def rebuildTree(prefixa, infixa):
    #Usa a primeira letra da prefixa como raiz, divide infixa ao redor dela e recorre.

    if not prefixa or not infixa:
        return None

    raiz_val = prefixa[0]
    raiz = No(raiz_val)
    i = infixa.index(raiz_val)

    raiz.esq = rebuildTree(prefixa[1:i+1], infixa[:i])
    raiz.dir = rebuildTree(prefixa[i+1:], infixa[i+1:])

    return raiz

def pos_ordem(no):
    if not no:
        return []
    return pos_ordem(no.esq) + pos_ordem(no.dir) + [no.valor]

def printTree(raiz, nivel=0):
    if raiz is not None:
        print('    ' * nivel + f'- {raiz.valor}')
        printTree(raiz.esq, nivel + 1)
        printTree(raiz.dir, nivel + 1)


def q2():
    #Prefixa: + Z Q * - / T L M
    #Infixa: Z + Q * (T / L - M)

    infixa = ['Z', '+', 'Q', '*', '(', 'T', '/', 'L', '-', 'M', ')']
    prefixa = ['+', 'Z', 'Q', '*', '-', '/', 'T', 'L', 'M']  # já resolvida entre parênteses

    # Limpando infixa para que seja diretamente comparável com prefixa
    infixa_filtrada = [x for x in infixa if x not in '()']

    arvore = rebuildTree(prefixa, infixa_filtrada)

    # Obter pósfixa
    posfixa = pos_ordem(arvore)
    print("Forma pósfixa:", ' '.join(posfixa))
    printTree(arvore)
    print("Complexidade: O(n) Estrutura: Arvore e Recursão")













#--------------------------------------------------------------------------------
if __name__ == "__main__":
    q1()