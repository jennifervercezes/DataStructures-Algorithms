# Declarando proprias estruturas básicas de dados
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Stack - Pilha é LiFo (Last in First Out), é simples e tem head e tail
# Sentido de Inserção/Next o------>

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def add(self,data):
        """add adiciona o dado na head - lastin da pilha"""

        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.head.next = newnode
            self.head = self.head.next
        
        self.len += 1

    def pop(self):
        """Remove o primeiro dado na head - lastin da pilha"""

        if self.head is None:
            print("The Stack is empty.")
            return None
        
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.len -= 1
        return data

    def peek(self):
        """Returns the lastin element without removing it."""

        if self.head is None:
            print("The Stack is empty.")
            return None

        return self.head.data

    def isempty(self):
        """Checks if the stack is empty."""
        return self.head is None

    def lenght(self):
        """Returns the number of elements in the stack."""
        return self.len

    def clear(self):
        """Clears the stack."""

        self.head = None
        self.tail = None
        self.len = 0




if __name__ == "__main__":

    stack = Stack()

    print("\n🔹 Test 1: add elements onto the stack")
    stack.add(10)
    stack.add(20)
    stack.add(30)
    print(f"Lastin element: {stack.peek()}")
    # Expected: 30

    print("\n🔹 Test 2: Pop element from the stack")
    print(f"Popped element: {stack.pop()}")
    # Expected: Popped element: 30

    print("\n🔹 Test 3: add more elements and see the top of the stack")
    stack.add(40)
    stack.add(50)
    print(f"Lastin element: {stack.peek()}")
    # Expected: 50

    print("\n🔹 Test 4: Lenght of the stack")
    print(stack.lenght())
    # Expected: 4

    print("\n🔹 Test 5: Pop all elements")
    stack.clear()
    print(
        f"Is stack empty? {stack.isempty()}. Number of nodes: {stack.lenght()}")
    # Expected: Is stack empty? True. Number of nodes: 0

    print("\n🔹 Test 6: Pop from empty stack")
    print(stack.pop())
    # Expected: The stack is empty. None

    print("\n🔹 Test 7: Peek in an empty stack")
    print(stack.peek())
    # Expected: The stack is empty. None

    print("\n🔹 Test 8: Lenght of the stack")
    print(stack.lenght())
    # Expected: 0