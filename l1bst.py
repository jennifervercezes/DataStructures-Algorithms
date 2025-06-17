class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None  # filho esquerdo
        self.dir = None  # filho direito

def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esq = inserir(raiz.esq, valor)
    elif valor > raiz.valor:
        raiz.dir = inserir(raiz.dir, valor)
    return raiz

def buscar(raiz, valor):
    if raiz is None or raiz.valor == valor:
        return raiz
    if valor < raiz.valor:
        return buscar(raiz.esq, valor)
    return buscar(raiz.dir, valor)

def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esq)
        print(raiz.valor, end=" ")
        em_ordem(raiz.dir)

def pre_ordem(raiz):
    if raiz:
        print(raiz.valor, end=" ")
        pre_ordem(raiz.esq)
        pre_ordem(raiz.dir)

def pos_ordem(raiz):
    if raiz:
        pos_ordem(raiz.esq)
        pos_ordem(raiz.dir)
        print(raiz.valor, end=" ")


#--------------------------------------------------------------------------------
if __name__ == "__main__":
    valores = [8, 3, 10, 1, 6, 14, 4, 7]
    raiz = None
    for v in valores:
        raiz = inserir(raiz, v)

    print("In-ordem (ordenado):") # 1 3 4 6 7 8 10 14
    print(f'{em_ordem(raiz)} \n {pos_ordem(raiz)} \n {pre_ordem(raiz)}')  
    
    

