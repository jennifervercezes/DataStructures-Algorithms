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

def fibonacciMemo(n, memo=None, contador=None):
    if memo is None:
        memo = {}
    if contador is None:
        contador = {'chamadas': 0}

    contador['chamadas'] += 1

    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacciMemo(n - 1, memo, contador) + fibonacciMemo(n - 2, memo, contador)

    return memo[n]

contador = {'chamadas': 0}
resultadoMemo = fibonacciMemo(10, contador=contador)
print(f"Resultado: {resultadoMemo}, Chamadas recursivas: {contador['chamadas']}")

resultadoIte = fibonacciIterativo(10)
print(f"Resultado: {resultadoIte}")