
'''Desenvolva  um  algoritmo que  faça a  conversão  da 
notação polonesa (prefixa) para a notação infixa. '''

def prefToInf(expr, op):
    pilha, result = [], []

    def montar():
        if len(result) >= 2 and pilha:
            operador = pilha.pop()
            a = result.pop()
            b = result.pop()
            result.append(a + operador + b)

    for char in expr: 
        
        if char in op: # operador
            while pilha and pilha[-1] != '(' and op.get(char) <= op.get(pilha[-1]):
                montar()
            pilha.append(char) 

        elif char == '(':
            pilha.append(char)

        elif char == ')':
            while pilha and pilha[-1] != '(':
                montar()
            pilha.pop()  # remove '('

        else:  # operando
            result.append(char)

    while pilha:
        montar()

    return result 



expr1 = list("*+ABC") 
expr2 = list("-+1/34*58")
op = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

result = prefToInf(expr2, op)
print(f' Prefixa {expr1}, Infixa {result}')
# Saída esperada: A+B*C
print("Complexidade O(n) para Tempo e Espaço") 