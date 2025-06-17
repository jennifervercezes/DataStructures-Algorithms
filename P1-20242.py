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

def isValid(j_ilha, c_ilha, j_cont, c_cont):
    # Verifica se em ambos os lados não há mais canibais que jesuítas
    cond1 = (j_ilha == 0 or j_ilha >= c_ilha)
    cond2 = (j_cont == 0 or j_cont >= c_cont)
    return cond1 and cond2

def evacuar(n):
    estado_inicial = (n, n, 0, 0, 'ilha')  
    # j_ilha, c_ilha, j_cont, c_cont, barco

    visitado = set()
    fila = deque([(estado_inicial, 0)])  
    # (estado, travessias)

    movimentos = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  
    # todas as formas de usar 1 ou 2 lugares]

    while fila:
        (j_ilha, c_ilha, j_cont, c_cont, barco), travessias = fila.popleft()

        if (j_ilha, c_ilha, j_cont, c_cont) == (0, 0, n, n):
            tempo_total = travessias * 10
            return tempo_total, travessias, n  
        # Todos salvos

        if (j_ilha, c_ilha, barco) in visitado:
            continue
        visitado.add((j_ilha, c_ilha, barco))

        for j, c in movimentos:
            if barco == 'ilha':
                novo_j_ilha = j_ilha - j
                novo_c_ilha = c_ilha - c
                novo_j_cont = j_cont + j
                novo_c_cont = c_cont + c
                novo_barco = 'continente'
            else:
                novo_j_ilha = j_ilha + j
                novo_c_ilha = c_ilha + c
                novo_j_cont = j_cont - j
                novo_c_cont = c_cont - c
                novo_barco = 'ilha'

            if 0 <= novo_j_ilha <= n and 0 <= novo_c_ilha <= n and \
               0 <= novo_j_cont <= n and 0 <= novo_c_cont <= n:
                if isValid(novo_j_ilha, novo_c_ilha, novo_j_cont, novo_c_cont):
                    fila.append(((novo_j_ilha, novo_c_ilha, novo_j_cont, novo_c_cont, novo_barco), travessias + 1))

    nsalvos = [(j_ilha - j_cont), (c_ilha - c_cont)]
    # Se chegou aqui, não é possível salvar todos
    return None, None, nsalvos

def q1():
    n = 14 # Numero de jesuítas = Numero de canibais
    tempo, viagens, salvos = evacuar(n)

    if tempo:
        print(f"Todos salvos em {tempo} minutos, usando {viagens} travessias.")
    else:
        print(f"Não é possível salvar os {n} jesuítas e {n} canibais.")
        print(f"Possível salvar até {salvos} jesuitas, canibais de cada lado.")

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
    q2()