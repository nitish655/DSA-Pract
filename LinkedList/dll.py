

class Node(self,value):
    self.value = value 
    self.next = None
    self.prev = None
    
class DoublyLL():
    
    def __init__(self):
        if not self.head:
            print("Linked List is empty")
            return
        
        self.head = Node()