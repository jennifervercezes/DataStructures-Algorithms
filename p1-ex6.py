
'''Implementar o algoritmo da Torre de Hanoi.'''

def hanoiRecursivo(n, origem='A', destino='C', auxiliar='B', contador=None):
    if contador is None:
        contador = {'chamadas': 0}

    contador['chamadas'] += 1

    if n == 1:
        print(f"Mover disco de {origem} para {destino}")
        return

    hanoiRecursivo(n - 1, origem, auxiliar, destino, contador)
    print(f"Mover disco de {origem} para {destino}")
    hanoiRecursivo(n - 1, auxiliar, destino, origem, contador)

    return contador['chamadas']

hanoiRecursivo(3, 'A', 'C', 'B')