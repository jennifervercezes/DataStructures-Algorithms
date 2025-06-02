'''Implemente: 
a. A versão não-recursiva para encontrar o número da 
n da sequência de Fibonacci. 
b. A  versão  recursiva  que  retorne  a  quantidade  de 
chamadas  recursivas  feitas.'''

def fibonacciIterativo(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacciMemo(n, contador, memo=None):
    if memo is None:
        memo = [None] * (n+1)

    contador[0] += 1

    if memo[n] is not None:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacciMemo(n - 1, contador, memo) + fibonacciMemo(n - 2, contador, memo)

    return memo[n]

contador = [0]
resultadoMemo = fibonacciMemo(10, contador)
print(f'\n Resultado: {resultadoMemo}, Chamadas recursivas: {contador}') 
print(" \n Recursividade com Memorização por Array \n Complexidade O(n) Tempo e O(n) Espaço")

resultadoIte = fibonacciIterativo(10)
print(f'\n Resultado: {resultadoIte}')
print(" \n Iteração em duas vars \n Complexidade O(n) Tempo e O(1) Espaço")