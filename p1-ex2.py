import random as rnd

'''Como poderemos achar uma celebridade em uma multidão, 
onde  todos  conhecem  a  celebridade  (que  não  conhece 
ninguém da multidão)? '''

def findCelebrity(party):
    n = len(party)
    stack = list(range(n))
    
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
    
        if party[a][b]:
            stack.append(b)  # a conhece b, então a não pode ser celebridade
        else:
            stack.append(a)  # a não conhece b, então b não pode ser celebridade

    candidate = stack.pop()
    
    # Verificação final do candidato
    for i in range(n):
        if i != candidate:
            
            if party[candidate][i] or not party[i][candidate]:
                return -1  # Não existe celebridade
    return candidate


def genParty(n):
    """Gera uma matriz NxN representando quem conhece quem na festa."""
    party = [[rnd.choice([True, False]) for _ in range(n)] for _ in range(n)]
    
    # Garantindo que ninguém conhece a si mesmo
    for i in range(n):
        party[i][i] = False

    # Escolhendo aleatoriamente uma celebridade
    celebrity = rnd.randint(0,n)
    for i in range(n):
        for j in range(n):
            if i == celebrity:
                party[i][j] = False  # Celebridade não conhece ninguém
            elif j == celebrity:
                party[i][j] = True  # Todos conhecem a celebridade

            else:
                party[i][j] = rnd.choice([True, False])

    return party, celebrity

n = 50 #numero de pessoas na festa
party, trueCelebrity = genParty(n)
foundCelebrity = findCelebrity(party)
print(f'foundCelebrity {foundCelebrity}, trueCelebrity {trueCelebrity}')
print("\n Pilha \n Complexidade: O(n)")