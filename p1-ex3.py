import random as rnd

'''Como podemos saber qual o candidato vence por maioria 
absoluta (50% + 1 voto) uma eleição?'''

def countVotes(votesList):
    stack = []
    
    for i in votesList:
        stack.append(i)

    currentCandidate = None
    counter = 0

    while len(stack) > 0:
        vote = stack.pop()
        if counter == 0:
            currentCandidate = vote
            counter = 1
        elif vote == currentCandidate:
            counter += 1
        else:
            counter -= 1

    return currentCandidate, counter


urna1 = [2]*58 + [1]*21 + [3]*15 + [4]*2 + [0]*4
rnd.shuffle(urna1)
listaVotos1 = urna1
print(listaVotos1)

urna2 = [4]*52 + [2]*17 + [1]*18 + [3]*10 + [0]*3
rnd.shuffle(urna2)
listaVotos2 = urna2
print(listaVotos2)

venceUrna1 = countVotes(listaVotos1)
venceUrna2 = countVotes(listaVotos2)

print(f'{venceUrna1}')
print(f'{venceUrna2}')
print("\n Boyer-Moore Majority Vote (Pilha) \n Complexidade O(n) Tempo e O(1) Espaço")