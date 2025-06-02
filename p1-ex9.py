'''Duas  empresas  abriram  falência,  onde  cada  empresa 
possui o mesmo grupo de credores que estão ávidos para 
ressarcirem seus prejuízos. A empresa P1 foi avaliada 
em R$ X,00. A empresa P2 foi avaliada em R$ Y,00. Note 
que  tanto  X  e  Y  são  valores  inteiros  e  positivos, 
diferentes de zero. O juiz responsável pela dissolução 
das empresas determina que o maior número possível de 
credores (Z) deverá receber o mesmo valor fixo, de cada 
empresa, onde Z é um valor inteiro e positivo, diferente 
de zero, se constituindo no maior divisor comum entre 
os valores de avaliação associados a cada empresa. Ou 
seja,  cada  credor  receberá  X/Z  +  Y/Z.  Descreva  um 
algoritmo que especifique o número máximo de credores 
(Z) que serão beneficiados com a decisão do judiciário.'''

def maxCredores(x,y):
    stack = []
    maxi = min(x,y)
    
    for i in range (1,maxi):
        
        if (x % i == 0) and (y % i == 0):
            stack.append(i)
            i += 1
        
        i += 1
    
    z = stack.pop()
    valuePerz = (x + y) / z
    return z, valuePerz

x = 18
y = 24
z, valuePerz = maxCredores(x,y) 
print(z, valuePerz, "\n Pilha \n Complexidade O(min(X, Y)) = O(n)")

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def Euclides(x, y):
    z = mdc(x, y)
    valuePerz = (x // z) + (y // z)

    return z, valuePerz

z, valuePerz = Euclides(x, y)
print(z, valuePerz, "\n Algoritmo de Euclides \n Complexidade O(log(min(X, Y))) = O(log(n))")