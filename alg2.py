import tkinter as tk
import random
import time

#white - possivel celebridade
#red - desclassificado
#yellow - segunda analise
#green - celebridade

def generate_party(n):
    """Gera uma matriz NxN representando quem conhece quem na festa."""
    party = [[random.choice([True, False]) for _ in range(n)] for _ in range(n)]
    
    # Garantindo que ninguém conhece a si mesmo
    for i in range(n):
        party[i][i] = False

    # Escolhendo aleatoriamente uma celebridade
    celebrity = random.randint(0, n - 1)
    for i in range(n):
        for j in range(n):
            if i == celebrity:
                party[i][j] = False  # Celebridade não conhece ninguém
            elif j == celebrity:
                party[i][j] = True  # Todos conhecem a celebridade

            else:
                party[i][j] = random.choice([True, False])

    return party, celebrity

def dfs_sink(knows, canvas, cells):
    n = len(knows)
    stack = list(range(n))  # Todos os candidatos
    
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        canvas.itemconfig(cells[a], fill='white')
        canvas.itemconfig(cells[b], fill='white')
        canvas.update()
        time.sleep(.1)
        
        if knows[a][b]:
            stack.append(b)  # a conhece b, então a não pode ser celebridade
            canvas.itemconfig(cells[a], fill='red')
        else:
            stack.append(a)  # a não conhece b, então b não pode ser celebridade

            canvas.itemconfig(cells[b], fill='red')

    candidate = stack.pop()
    
    # Verificação final do candidato
    for i in range(n):
        if i != candidate:
            canvas.itemconfig(cells[i], fill='yellow')
            canvas.update()
            time.sleep(.03)
            
            if knows[candidate][i] or not knows[i][candidate]:
                canvas.itemconfig(cells[candidate], fill='red')
                return -1  # Não existe celebridade
    
    canvas.itemconfig(cells[candidate], fill='green')
    return candidate

def visualize():
    n = 101
    party, true_celebrity = generate_party(n)
    root = tk.Tk()
    root.title("Busca pela Fernanda Torres")
    canvas = tk.Canvas(root, width= (n * 8), height= ((2*n - 1) * 2.5))
    canvas.pack()

    cells = []
    for i in range(n):
        x = 20 + (i % 15) * 50
        y = 50 + (i // 15) * 60
        cell = canvas.create_rectangle(x, y, x + 50, y + 50, fill="gray", outline="white")
        cells.append(cell)
        canvas.create_text(x + 25, y + 25, text=str(i), font=("Arial", 10))
    
    celebrity = dfs_sink(party, canvas, cells)

    if celebrity != -1:
        result = f"Celebridade encontrada: {celebrity}"
    else:
        result = "Nenhuma celebridade encontrada"

    canvas.create_text(400, 20, text=result, font=("Arial", 14), fill="blue")
    canvas.create_text(400, 40, text=f"Celebridade real: {true_celebrity}", font=("Arial", 12), fill="gray")

    root.mainloop()

visualize()
