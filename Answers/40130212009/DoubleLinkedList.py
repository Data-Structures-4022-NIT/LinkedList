class Node:
    def __init__(self, value):
        # Initialize a new node with the given value
        self.value = value
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list

class DoublyLinkedList:
    def __init__(self):
        # Initialize an empty doubly linked list
        self.head = None  # Pointer to the first node in the list
        self.tail = None  # Pointer to the last node in the list

    def insert_in_front(self, value):
        # Insert a new node with the given value at the front of the list
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insert_in_back(self, value):
        # Insert a new node with the given value at the back of the list
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def search(self, value):
        # Search for a node with the given value in the list
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index  # Return the index of the node if found
            index += 1
            current = current.next
        return 'Not Found!'  # Return 'Not Found!' if the value is not in the list
    
    def delete_at_front(self):
        # Delete the node at the front of the list and return its value
        if not self.head:
            return None
        deleted_node = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node

    def delete_at_back(self):
        # Delete the node at the back of the list and return its value
        if not self.head:
            return None
        if self.head == self.tail:
            deleted_node = self.head.value
            self.head = self.tail = None
            return deleted_node
        deleted_node = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return deleted_node

    def size(self):
        # Calculate and return the size (number of nodes) of the list
        num = 0
        current = self.head
        while current:
            num += 1
            current = current.next
        return num
    
    def clear(self):
        # Clear the list by setting head and tail to None
        self.head = None
        self.tail = None

    def print_forward(self):
        # Print the values of the list from head to tail
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print('None')

    def print_backward(self):
        # Print the values of the list from tail to head
        current = self.tail
        while current:
            print(current.value, end=' ')
            current = current.prev
        print('None')

    def make_doubly(self, singly_list):
        # Convert a singly linked list to a doubly linked list
        doubly_list = DoublyLinkedList()
        if not singly_list.head:
            return 'The list is empty!'
        current = singly_list.head
        previous = None
        while current:
            current.prev = previous
            previous = current
            current = current.next

    def reverse_non_recursive(self):
        # Reverse the list in place non-recursively
        if not self.head or not self.head.next:
            return self.head

        p = None
        current = self.head
        while current:
            next_node = current.next
            current.next = p
            current.prev = next_node
            p = current
            current = next_node
        self.head = p
        return self.head

# Example usage of DoublyLinkedList

# Create a new doubly linked list
dll = DoublyLinkedList()

# Insert elements at the front of the list
dll.insert_in_front(10)
dll.insert_in_front(20)
dll.insert_in_front(30)

# Print the list forward
print("List after inserting 30, 20, 10 at the front:")
dll.print_forward()  # Output: 30 20 10 None

# Insert elements at the back of the list
dll.insert_in_back(40)
dll.insert_in_back(50)

# Print the list forward
print("List after inserting 40, 50 at the back:")
dll.print_forward()  # Output: 30 20 10 40 50 None

# Print the list backward
print("List printed backward:")
dll.print_backward()  # Output: 50 40 10 20 30 None

# Search for an element in the list
print("Search for value 20:")
print(dll.search(20))  # Output: 1

print("Search for value 60:")
print(dll.search(60))  # Output: Not Found!

# Delete elements at the front and back of the list
print("Delete at front:")
print(dll.delete_at_front())  # Output: 30

print("Delete at back:")
print(dll.delete_at_back())  # Output: 50

# Print the list forward after deletions
print("List after deleting front and back:")
dll.print_forward()  # Output: 20 10 40 None

# Get the size of the list
print("Size of the list:")
print(dll.size())  # Output: 3

# Clear the list
dll.clear()
print("List after clearing:")
dll.print_forward()  # Output: None

# Insert more elements to demonstrate reversing the list
dll.insert_in_front(1)
dll.insert_in_back(2)
dll.insert_in_back(3)
dll.insert_in_back(4)

# Print the list before reversing
print("List before reversing:")
dll.print_forward()  # Output: 1 2 3 4 None

# Reverse the list
dll.reverse_non_recursive()
print("List after reversing:")
dll.print_forward()  # Output: 4 3 2 1 None
