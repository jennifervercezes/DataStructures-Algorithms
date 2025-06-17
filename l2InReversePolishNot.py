
'''Desenvolva  um  algoritmo que  faça a  conversão  da 
notação  polonesa  reversa  (pósfixa)  para  a  notação 
infixa.'''

def posToInf(expr):
    pilha = []

    for char in expr:
        if char.isalnum():  # Operando, ou fazer char.isalnum()
            pilha.append(char)
        else:  # Operador
            a = pilha.pop()
            b = pilha.pop()
            pilha.append(b + char + a)

    return pilha


if __name__ == "__main__":
    expr1 = list("AB+C*") 
    expr2 = list("134/+58*-")
    op = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    result = posToInf(expr2)
    print(f' Posfixa {expr2}, Infixa {result}')
    # Saída esperada: A+B*C
    print("Complexidade O(n) para Tempo e Espaço") 