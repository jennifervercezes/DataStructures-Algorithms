
'''Implementar o algoritmo da Torre de Hanoi.'''

def hanoiRecursivo(n, origem='A', destino='C', auxiliar='B', contador = [0]):

    contador[0] += 1

    if n == 1:
        print(f"Mover disco de {origem} para {destino}")
        return

    hanoiRecursivo(n - 1, origem, auxiliar, destino, contador)
    print(f"Mover disco de {origem} para {destino}")
    hanoiRecursivo(n - 1, auxiliar, destino, origem, contador)

    return contador[0]

hanoiRecursivo(3, 'A', 'C', 'B')
print("\n Recursividade com O(n) Profundidade\n Complexidade O(2^n) Tempo e O(1) Memória")