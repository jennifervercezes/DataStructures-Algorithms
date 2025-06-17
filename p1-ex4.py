
'''Como  nosso  celular  encontra  o  nome  de  um  contato 
armazenado  na  agenda?  (dica:  a  lista  de  nomes  está 
ordenada)'''

contatos = ["Ana", "Carlos", "Celia", "Daniela", "João", "JP", "Luísa", "Pedro", "Xandra"]

def buscaBinaria(nome, listaContatos):
    inicio = 0
    fim = len(listaContatos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if listaContatos[meio] == nome:
            return meio  # encontrou!
        elif listaContatos[meio] < nome:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1  # não encontrou

indice = buscaBinaria("João", contatos)

if indice != -1:
    print(f"Contato encontrado na posição {indice}")
else:
    print("Contato não encontrado")

print("\n Busca Binária em Array \n Complexidade: \n Se Ordenado: O(log(n)) \n Se há de Ordenar com Merge/Quick: O(nlog(n))")