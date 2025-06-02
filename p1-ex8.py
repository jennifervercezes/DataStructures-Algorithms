
'''Desenvolva um algoritmo que determine se um número p
informado é primo e informe os dois primos antecessores 
e os dois primos sucessores de p.'''

def isPrime(p):

    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False

    i = 3
    while i * i <= p:
        if p% i == 0:
            return False
        i += 2
    return True
  
def primeList(p, maxlen):
    primeBeforeP = []
    pMinus1 = p - 1
    
    while len(primeBeforeP) < maxlen and pMinus1 > 1:
        if isPrime(pMinus1):
            primeBeforeP.insert(0, pMinus1)  # Insere no início
        pMinus1 -= 1

    primeAfterP = []
    pPlus1 = p + 1
    
    while len(primeAfterP) < maxlen:
        if isPrime(pPlus1):
            primeAfterP.append(pPlus1)
        pPlus1 += 1
    
    return primeBeforeP, primeAfterP

p = 67
print(isPrime(p))
print(primeList(p,2))
print("\n Lista Encadeada Simples \n Complexidade O(n)")