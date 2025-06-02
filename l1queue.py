# Declarando proprias estruturas básicas de dados
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Queue - Fila é FiFo (First in First Out), é simples e tem head e tail
# Sentido de Inserção/Next <------o
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def add(self,data):
        """Add adiciona o dado na tail - lastin da fila"""

        newnode = Node(data)
        
        if self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = self.tail.next
    
        self.len += 1

    def pop(self):
        """Remove o primeiro dado na head - firstin da fila"""

        if self.head is None:
            print("The Queue is empty.")
            return None
        
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.len -= 1
        return data
    
    def peek(self):
        """Returns the firstin element without removing it."""

        if self.head is None:
            print("The Queue is empty.")
            return None

        return self.head.data

    def isempty(self):
        """Checks if the queue is empty."""
        return self.head is None

    def length(self):
        """Returns the number of elements in the queue."""
        return self.len

    def clear(self):
        """Clears the queue."""

        self.head = None
        self.tail = None
        self.len = 0




if __name__ == "__main__":

    queue = Queue()

    print("\n🔹 Test 1: add elements into the queue")
    queue.add(10)
    queue.add(20)
    queue.add(30)
    print(f"Front element: {queue.peek()}")
    # Expected: Front element: 10

    print("\n🔹 Test 2: Pop element from the queue")
    print(f"Popped element: {queue.pop()}")
    # Expected: Popped element: 10

    print("\n🔹 Test 3: add more elements and check the front of the queue")
    queue.add(40)
    queue.add(50)
    print(f"Front element: {queue.peek()}")
    # Expected: Front element: 20

    print("\n🔹 Test 4: Length of the queue")
    print(f"Queue size: {queue.length()}")
    # Expected: Queue size: 4

    print("\n🔹 Test 5: Pop all elements")
    print(
        f"Is queue empty? {queue.isempty()}. Number of elements: {queue.length()}")
    # Expected: Is queue empty? False. Number of elements: 4
    print("Clear the queue.")
    queue.clear()
    print(
        f"Is queue empty? {queue.isempty()}. Number of elements: {queue.length()}")
    # Expected: Is queue empty? True. Number of elements: 0

    print("\n🔹 Test 6: Pop from an empty queue")
    print(queue.pop())
    # Expected: The queue is empty. None

    print("\n🔹 Test 7: Peek into an empty queue")
    print(queue.peek())
    # Expected: The queue is empty. None

    print("\n🔹 Test 8: Length of the queue")
    print(f"Queue size: {queue.length()}")
    # Expected: Queue size: 0