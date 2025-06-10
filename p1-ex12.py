
'''Desenvolva  um  algoritmo que  faça a  conversão  da 
notação infixa para a notação polonesa (prefixa).'''

def infToPref(expr, op):
    pilha, result = [], []

    def montar():
        if len(result) >= 2 and pilha:
            operador = pilha.pop()
            a = result.pop()
            b = result.pop()
            result.append(operador + b + a)

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



expr1 = list("(A+B)*C") 
expr2 = list("1+(3/4)-(5*8)")
op = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

result = infToPref(expr2, op)
print(f' Prefixa {result}, Infixa {expr2}')
# Saída esperada: *+ABC
print("Complexidade O(n) para Tempo e Espaço")  
