# Menu driven Singly Linked List
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 
        
class LinkedList():
    def __init__(self):
        self.head = None       # Initially head is None
        self.size = 0
        
    def __len__(self):
        return self.size
        
    # adding elements
    def insert_at_end(self, value):
        new_node = Node(value)
        
        '''
        If the LL is empty and just create head is
        pointing to the node
        '''
        if not self.head:           
            self.head = new_node    
            self.size += 1
            print(f"Inserted {value} at the beginning")
            return
            
        # initialising new variable called last and storing head in it
        # last will be used for traversal
        
        last = self.head
        
        # while loop --> loop unless the next is None
        
        while  last.next:
            last = last.next
        last.next = new_node
        self.size += 1
        print(f'Inserted {value} at the end')
        print(f'Length of Linked List after adding at end position is {len(l)}')
        
    def insert_at_specific(self,index,value):
        if index < 0 or index > self.size:
            print('Invalid Syntax')
            return
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            print(f'Inserted {value} at position {index}')
            print(f'Length of Linked List now is {len(l)}')
            return
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        print(f'Inserted {value} at position {index}')
        print(f'Length of Linked List is {len(l)}')
        
    def display(self):
        if not self.head:
            print(f'Linked list is empty')
            return
        current = self.head
        while current:
            #print(f"{current.value}| {current.next} --> ",end="")
            print(f"{current.value} --> ",end="")
            current = current.next
        print('None')
        print(f'Length of Linked List is {len(l)}')
        
        
    def search(self, element):
        if not self.head:
            print(f'Linked list is empty')
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
        
        
    def delete_from_start(self):
        if not self.head:
            print('Linked List is Empty ')
            return
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        print(f'Deleted {val} from linked list')
        l.display()
        print(f'Length of Linked List after deleting from start is {len(l)}')
        
    def delete_from_end(self):
        if not self.head:
            print('Linked List is empty')
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
        l.display()
        print(f'Length of Linked List after deleting from end is {len(l)}')
        
    def delete(self, key):
        if not self.head:
            print('Linked List is Empty')
            return
        if self.head.value == key:
            self.head = self.head.next
            self.size -= 1
            print('Deleted Element')
            print(f'Length of Linked List now is {len(l)}')
            return
        current = self.head
        while current.next:
            if current.next.value == key:
                current.next = current.next.next
                self.size -= 1
                print('Deleted Element')
                print(f'Length of Linked List now is {len(l)}')
                return
            
            current = current.next                  # Moving Pointer
        print('Element not found')
        l.display()
            
        
    def show_menu(self):
        print("\n-- Linked List Menu --")
        print("1. Insert Element ")
        print("2. Display Linked List")
        print("3. Search in Linked List")
        print('4. Delete element from start')
        print('5. Delete element from end')
        print('6. Delete a specific element')
        print('7. Insert element at particular index')
        print("8. Exit ")
        
        
l = LinkedList()

while True:
    l.show_menu()
    choice = input('Enter your choice : ')
    if choice == '1':
        data = int(input('Enter the element to insert: '))
        l.insert_at_end(data)
    
    elif choice == '2':
        l.display()
        
    elif choice == '3':
        element = int(input('Enter the element to search: '))
        l.search(element)
        
    elif choice == '4':
        l.delete_from_start()
        
    elif choice == '5':
        l.delete_from_end()
        
    elif choice == '6':
        key = int(input('Enter the value you want to delete: '))
        l.delete(key)
        
    elif choice == '7':
        data = int(input('Enter the element to insert: '))
        idx = int(input('Enter the position (0-based index): '))
        l.insert_at_specific(idx, data)        
        
    elif choice == '8':
        print('Exiting...')
        break
    
    
    
    
    
# l.display()
# l.insert_at_end(3)
# l.insert_at_end(51)
# l.insert_at_end(75)
# l.insert_at_end(97)
# l.insert_at_end(115)
# l.insert_at_end(132)
# l.insert_at_end(151)
# l.display()