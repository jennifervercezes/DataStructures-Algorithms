# Declarando proprias estruturas básicas de dados
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# Single Link List - Lista Encadeada Simples, é simples e tem head e tail
# Sentido de Inserção//Next ------>o------>
class SingleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def addNext(self,data):
        
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.head.next = newnode
            self.head = self.head.next
        
        self.len += 1

    def addLast(self,data):
        newnode = Node(data)

        if self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = self.tail.next
        
        self.len += 1

    def addatPos(self,data):
        newnode = Node(data)

        if self.tail is None or self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            current = self.head
            self.tail.next = newnode
            self.tail = self.tail.next
        
        self.len += 1

    def popNext(self):
        
        if self.head is None:
            print("The Deck is Empty")
            return None
        
        data = self.head.data
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self.len -= 1
        return data


    def popLast(self):
        
        if self.tail is None:
            print("The Deck is Empty")
            return None
        
        data = self.tail.data
        self.tail = self.tail.next

        if self.tail is None:
            self.head = None
        
        self.len -= 1
        return data
    
    def popatPos(self):
        a=1

    def peekList(self):
        """Prints the linked list node by node."""

        if self.head is None:
            print("The linked list is empty.")
            return None

        else:
            current = self.head

            while current:
                print(current.data, "-> ", end='')
                current = current.next

            print("None")
    
    def search(self, data) -> tuple[bool, int]:
        a=1
    
    def isempty(self):
        """Checks if the deck is empty."""
        return self.head is None

    def length(self):
        """Returns the number of elements in the deck."""
        return self.len

    def clear(self):
        """Clears the deck."""

        self.head = None
        self.tail = None
        self.len = 0




if __name__ == "__main__":

    sll = SingleLinkList()

    print("\n🔹 Test 1: Insert at the beginning")
    sll.addLast(30)
    sll.addLast(20)
    sll.addLast(10)
    sll.peekList()  
    # Expected: 10 -> 20 -> 30 -> None

    print("\n🔹 Test 2: Insert at the end")
    sll.addNext(40)
    sll.addNext(50)
    sll.peekList()  
    # Expected: 10 -> 20 -> 30 -> 40 -> 50 -> None

    print("\n🔹 Test 3: Insert at position (index 2)")
    sll.addtoPos(25, 2)
    sll.peekList()  
    # Expected: 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> None

    print("\n🔹 Test 4: Remove from the beginning")
    sll.popNext()
    sll.peekList()  
    # Expected: 20 -> 25 -> 30 -> 40 -> 50 -> None

    print("\n🔹 Test 5: Remove from the end")
    sll.popLast()
    sll.peekList()  
    # Expected: 20 -> 25 -> 30 -> 40 -> None

    print("\n🔹 Test 6: Remove from position (index 2)")
    sll.popatPos(2)
    sll.peekList()  
    # Expected: 20 -> 25 -> 40 -> None

    print("\n🔹 Test 7: Search for an existing element (25)")
    found, position = sll.search(25)
    print(f"Element 25 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 25 found at position 1

    print("\n🔹 Test 8: Search for a non-existing element (100)")
    found, position = sll.search(100)
    print(f"Element 100 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 100 not found at position -1

    print("\n🔹 Test 9: Remove from an out-of-range position (index 10)")
    sll.popatPos(10)
    # Expected: "Index error: out of range of the linked list."

    print("\n🔹 Test 10: Number of nodes")
    print(sll.lenght())  
    # Expected: 3

    print("\n🔹 Test 11: Remove all elements until the list is empty")
    sll.popNext()
    sll.popNext()
    sll.popNext()
    sll.peekList()  
    # Expected: The linked list is empty.

    print("\n🔹 Test 12: Search in an empty list")
    found, position = sll.search(30)
    print(f"Element 30 {'found' if found else 'not found'} at position {position}")
    # Expected: Element 30 not found at position -1