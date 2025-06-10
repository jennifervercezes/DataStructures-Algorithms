
'''Implementar  um  algoritmo  para  identificar  a 
quantidade  de  palíndromos  presentes  em  um  texto.  Os 
palíndromos  podem  ser  palavras,  frases  ou  o  próprio 
texto. Utilize para separar as frases a pontuação de 
vírgula, ponto ou ponto final, pontos de exclamação e 
pontos de interrogação.'''

from collections import deque

def is_palindrome(word):
    if len(word) <= 1:
        return False  # Ignorar palavras de 1 char
    return word == word[::-1]

def findPalind(d, s, sep): #deque, string,separadores
    count = 0
    phrases = []
    temp = ""

    # Separar frases com base nos separadores
    for char in s:
        if char not in sep:
            temp += char
        else:
            if temp:
                phrases.append(temp.strip().lower())
                temp = ""
    if temp:
        phrases.append(temp.strip().lower())  # adicionar o último trecho, se existir

    seen = set()  # Para evitar duplicatas

    # Quebra cada frase em palavras e verifica palíndromos
    for phrase in phrases:
        d.clear()
        for c in phrase:
            d.append(c)
        full = ''.join(d)
        if is_palindrome(full) and full not in seen:
            count += 1
            seen.add(full)

        # Verifica palavras
        words = phrase.split()
        for word in words:
            if is_palindrome(word) and word not in seen:
                count += 1
                seen.add(word)

    return count

# Testes
s1 = "roma é amor!adoro ovo.mirim"
s2 = "renner?cabide"
sep = ["!", "?", ".", ","]

d1 = deque()
d2 = deque()

print(f'\n {s1} -> {findPalind(d1, s1, sep)} palíndromos')
print(f'\n {s2} -> {findPalind(d2, s2, sep)} palíndromos')
print(" \n Deque e Lista \n Complexidade O(n*k) com k constante")