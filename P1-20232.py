'''
1ª Questão:
Desenvolva um algoritmo que, dado as sequências de nós nas ordens SIMÉTRICA 
E PREORDEM, seja capaz de reconstruir a arvore binária.
Aplique o algoritmo proposto para reconstruir (faça o esquema da árvore) 
a árvore referente binária (OHPDQIRBJESKTAFCUMGVNZX) às ordens e
SIMÉTRICA PREORDEM (ABDHOPIQREJKSTCFGMUNVXZ). 
Analise a complexidade do algoritmo proposto e diga se o mesmo é dito um algoritmo ótimo.

2a Questão:
Desenvolva um algoritmo que, dado um texto, faça a identificação do total de palíndromos existentes de palavra e de frases, separadamente.
Exemplo para palíndromo de palavras: HANNAH
Exemplo de palíndromo de frase: ROMA ME TEM AMOR
Analise a complexidade do algoritmo proposto e diga se o mesmo é dito um algoritmo ótimo.

3a Questão:
Desenvolva UM ÚNICO algoritmo RECURSIVO que transforme uma função matemática escrita na forma PRÉFIXA para as formas INFIXA e POSFIXA.
Analise a complexidade do algoritmo proposto e diga se o mesmo é dito um algoritmo ótimo'''

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def buildTree(pre_ordem, in_ordem):
    if not pre_ordem or not in_ordem:
        return None

    raiz_valor = pre_ordem[0]
    raiz = Node(raiz_valor)

    i = in_ordem.index(raiz_valor)

    raiz.esq = buildTree(pre_ordem[1:i+1], in_ordem[:i])
    raiz.dir = buildTree(pre_ordem[i+1:], in_ordem[i+1:])

    return raiz

def printTree(raiz, nivel=0):
    if raiz is not None:
        print('    ' * nivel + f'- {raiz.valor}')
        printTree(raiz.esq, nivel + 1)
        printTree(raiz.dir, nivel + 1)


def q1():
    #Entradas fornecidas pela questão
    pre_ordem = list("ABDHOPIQREJKSTCFGMUNVXZ")
    in_ordem = list("OHPDQIRBJESKTAFCUMGVNZX")

    # Reconstrução da árvore
    arvore = buildTree(pre_ordem, in_ordem)

    # Impressão textual da árvore
    print(f'Árvore reconstruída: {printTree(arvore)}')
    print("Complexidade: O(n²) Estrutura: Arvore e Recursão")












#--------------------------------------------------------------------------------
import re

def limpar_texto(texto):
    # Remove acentos e transforma em maiúsculo
    import unicodedata
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto.upper()

def eh_palindromo(texto):
    texto = texto.replace(" ", "")
    return texto == texto[::-1]

def contar_palindromos(texto):
    texto_limpo = limpar_texto(texto)

    # Palavras
    palavras = re.findall(r'\b\w+\b', texto_limpo)
    palindromos_palavras = [p for p in palavras if len(p) > 1 and p == p[::-1]]

    # Frases (separamos por pontuação ou quebra de linha como frases)
    frases_raw = re.split(r'[.!?\\n]', texto)
    frases = [f.strip() for f in frases_raw if len(f.strip()) > 0]
    palindromos_frases = [
        f for f in frases
        if eh_palindromo(limpar_texto(f)) and len(f.strip().replace(' ', '')) > 1
    ]

    return len(palindromos_palavras), len(palindromos_frases)

def q2():
    texto = """
    Hannah viu o radar. Roma me tem amor.
    Será que o ovo viu a Ana? Isso é um palíndromo!
    """

    palavras, frases = contar_palindromos(texto)
    print(f"Palavras palíndromas: {palavras}")
    print(f"Frases palíndromas: {frases}")











#--------------------------------------------------------------------------------
from l2InPolishNot import prefToInf

def prefix_to_infix_postfix(expr, op):
    def rec(index):
        char = expr[index]

        # Se for operador, então processa recursivamente os dois operandos
        if char in op:
            left_expr, left_index = rec(index + 1)
            right_expr, right_index = rec(left_index)

            infix = f"({left_expr[0]}{char}{right_expr[0]})"
            postfix = f"{left_expr[1]}{right_expr[1]}{char}"

            return (infix, postfix), right_index
        else:
            # Se for operando, apenas retorna
            return (char, char), index + 1

    (infix, postfix), _ = rec(0)
    return infix, postfix


def q3():
    expr = list("*+ABC")
    op = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    
    print(expr)

    print(prefToInf(expr))   
    print(prefix_to_infix_postfix(expr,op))
    

    print("Complexidade O(n) e Estrutura: Pilha")









#--------------------------------------------------------------------------------
if __name__ == "__main__":
    q1()