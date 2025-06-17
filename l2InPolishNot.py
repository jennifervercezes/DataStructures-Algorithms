
'''Desenvolva  um  algoritmo que  faça a  conversão  da 
notação polonesa (prefixa) para a notação infixa. '''

def prefToInf(expr):
    pilha = []

    for char in reversed(expr):
        if char.isalnum():  # Operando, ou fazer char.isalnum()
            pilha.append(char)
        else:  # Operador
            a = pilha.pop()
            b = pilha.pop()
            pilha.append(a + char + b)

    return pilha


if __name__ == "__main__":
    expr1 = list("*+ABC") 
    expr2 = list("-+1/34*58")
    op = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    result = prefToInf(expr2)
    print(f' Prefixa {expr2}, Infixa {result}')
    # Saída esperada: A+B*C
    print("Complexidade O(n) para Tempo e Espaço") 