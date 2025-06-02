
'''Implementar um algoritmo que, dado duas listas com os 
coeficientes  de  dois  polinômios,  retorne  a  soma  do 
polinômio com seus coeficientes em uma lista.'''

P = [3, 2, 5]
Q = [456, 34]

def somaPolinomios(P, Q):
    resultado = []

    for i in range(max(len(P), len(Q))):
        coef1 = P[i] if i < len(P) else 0
        coef2 = Q[i] if i < len(Q) else 0
        resultado.append(coef1 + coef2)

    return resultado

print(somaPolinomios(P, Q))