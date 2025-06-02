# Declarando proprias estruturas básicas de dados
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Deck - deck é duplo e tem head e tail
# Sentido de Inserção/Last/Next <------o------>
class Deck:
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

    def peekNext(self):
        
        if self.head is None:
            print("The Deck is empty.")
            return None

        return self.head.data
    
    def peekLast(self):
        
        if self.tail is None:
            print("The Deck is empty.")
            return None

        return self.tail.data
    
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

    deck = Deck()

    print("\n🔹 Test 1: Push elements to the front and back of the deck")
    deck.addNext(10)
    deck.addNext(20)
    deck.addLast(30)
    deck.addLast(40)
    print(f"Front element: {deck.peekNext()}")
    # Expected: Front element: 20
    print(f"Back element: {deck.peekLast()}")
    # Expected: Back element: 40

    print("\n🔹 Test 2: Pop element from the front")
    print(f"Popped front element: {deck.popNext()}")
    # Expected: Popped front element: 20

    print("\n🔹 Test 3: Push more elements and check the deck")
    deck.addNext(50)
    deck.addLast(60)
    print(f"Front element: {deck.peekNext()}")
    # Expected: Front element: 50
    print(f"Back element: {deck.peekLast()}")
    # Expected: Back element: 60

    print("\n🔹 Test 4: Length of the deck")
    print(f"deck size: {deck.length()}")
    # Expected: deck size: 5

    print("\n🔹 Test 5: Clear all elements")
    deck.clear()
    print(
        f"Is deck empty? {deck.isempty()}. Number of elements: {deck.length()}")
    # Expected: Is deck empty? True. Number of elements: 0

    print("\n🔹 Test 6: Pop from front and back an empty deck")
    print(deck.popNext())
    # Expected: None
    print(deck.popLast())
    # Expected: None

    print("\n🔹 Test 7: Peek front and back into an empty deck")
    print(deck.peekNext())
    # Expected: None
    print(deck.peekLast())
    # Expected: None

    print("\n🔹 Test 8: Length of the deck")
    print(f"deck size: {deck.length()}")
    # Expected: deck size: 0