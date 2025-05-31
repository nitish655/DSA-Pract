class Node():
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None
    
class DoublyLL():
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        # curr = self.head
        # while curr:
        #     curr = curr.next
        return self.size
        
    
    def insert_at_end(self,value):
        new_node = Node(value)
        
        if not self.head:
            self.head = new_node
            self.size += 1
            print(f'Inserted {value} at the beginning since it was empty')
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        self.size += 1
        print(f'Inserted {value} at the end')
        
        
    def insert_at_start(self,value):
        if not self.head:           
            self.head = Node(value)    
            print(f"Inserted {value} at the beginning")
            return
        
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1
        print(f"Inserted {value} at the beginning")
    
    
    def insert_at_specific(self,index,value):
        if index < 0 or index > self.size:
            print('Invalid Syntax')
            return
        
        new_node = Node(value)  
        if index == 0:
            self.insert_at_start()
            return
        
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.prev = current
        new_node.next = current.next
        current.next = new_node   
                
        if current.next:
            current.next.prev = new_node
            current.next = new_node
            self.size += 1
            print(f'Inserted {value} at position {index}')    
            
        
    def search(self,element):
        if not self.head:
            print(f'Linked List is empty')
            return
        
        counter = 0
        current = self.head
        while current:
            counter = counter + 1
            if current.value == element:
                print(f"Element found in Linked List at node {counter}")
                return
            current = current.next
        print('Element not found')
        
        
    def display(self):
        if not self.head:
            print('Linked List is empty')
            return
        
        current = self.head
        while current:
            print(f'{current.value} <--> ',end='')
            #print(f'{current.prev}|{current.value} | {current.next} | <--> ',end='')
            current = current.next
            
        print('None')
        
    def display_reverse(self):
        if not self.head:
            print(f'Linked List is empty')
            return
        
        # Go to the last node
        current = self.head
        while current.next:
            current = current.next
            
        # Traverse backwards using previous pointer
        
        while current:
            print(f'{current.value} <--> ', end='')
            current = current.prev
            
        print('None')
        
        
    def delete_from_start(self):
        if not self.head:
            print('List is empty')
            return
        val = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        print(f'Deleted {val} from linked list')
        self.display()
    
    
    def delete_from_end(self):
        if not self.head:
            print('List is empty')
            return
        
        if not self.head.next:
            self.head = None
            self.size -= 1
            print('Deleted the only element in Linked List')
            print(f'Length of Linked List is {len(l)}')
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.value
        current.next = None
        self.size -= 1
        print(f'Deleted {data} from end')
        dll.display()
    
    
    def deletion_from_value(self, key):
        if not self.head:
            print('Linked List is Empty')
            return
        current = self.head
        while current:
            if current.value == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                self.size -= 1
                print('Deleted Element')
                print(f'Length of Linked List now is {len(self)}')
                self.display()
                return
            
            current = current.next
        print('Element not found')
        
            
    def deletion_from_position(self, pos):
       
        if not self.head:
            print('Linked List is Empty')
            return
        if pos < 0 or pos >= self.size:
            print('Invalid Position')
            return
        if pos == 0:
            self.delete_from_start()
            return

        current = self.head
        for _ in range(pos):
            current = current.next

        # Remove current node
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

        self.size -= 1
        print(f'Deleted element at position {pos}')
        self.display()
        
        
    def show_menu(self):        
        print('\n -- Doubly Linked List Menu -- ')
        print('1.  Insert element at start')
        print('2.  Insert element at end')
        print('3.  Insert element at specific position')
        print('4.  Display Linked List') 
        print('5.  Display Reverse of Linked List')  
        print('6.  Search in Linked List')
        print('7.  Delete element from start')
        print('8.  Delete element from end')
        print('9.  Delete a specific element by value')
        print('10. Delete a specific element by position')
        print('11. Exit ')         
                
         
dll = DoublyLL()
while True:
    dll.show_menu()
    choice = input('Enter your choice: ') 
    
    if choice == '1':
        data = int(input('Enter the element to insert: '))
        dll.insert_at_start(data)
    
    elif choice == '2':
        data = int(input('Enter the element to insert: '))
        dll.insert_at_end(data)
        
    elif choice == '3':
        data = int(input('Enter the element to insert: '))
        idx = int(input('Enter the position (0-based index): '))
        dll.insert_at_specific(idx,data)
        
    elif choice == '4':
        dll.display()
        
        
    elif choice == '5':
        dll.display_reverse()
        
    elif choice == '6':
        element = int(input('Enter the element to search: '))
        dll.search(element)
        
    elif choice == '7':
        dll.delete_from_start()
        
    elif choice == '8':
        dll.delete_from_end()
        
    elif choice == '9':
        key = int(input('Enter the element to delete: '))
        dll.deletion_from_value(key)
        
    elif choice == '10':
        pos = int(input('Enter the position tou want to delete: '))
        dll.deletion_from_position(pos)
        
    elif choice == '11':
        print('Exiting...')
        break
                  
            
# dll = DoublyLL()
# a = dll.insert_at_end(5)
# b = dll.insert_at_end(8)
# c = dll.insert_at_end(16)
# d = dll.insert_at_end(25)
# print(len(dll))
# dll.display()
# dll.insert_at_start(85)
# dll.display()
# dll.insert_at_specific(2,52)
# dll.display()
# dll.display_reverse()
# dll.search(16)
# print(a)
# print(b)