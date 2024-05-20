class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node in the list

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty list with head as None
        
    def insert_in_back(self, value):
        """Insert a new node with the given value at the back of the list."""
        new_node = Node(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node  # Link the new node at the end

    def insert_in_front(self, value):
        """Insert a new node with the given value at the front of the list."""
        new_node = Node(value)
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node

    def delete_at_back(self):
        """Delete the node at the back of the list and return its value."""
        if not self.head:  # If the list is empty
            return None
        if not self.head.next:  # If there is only one node in the list
            deleted_node = self.head.value
            self.head = None  # List becomes empty
            return deleted_node
        current = self.head
        while current.next.next:  # Traverse to the second last node
            current = current.next
        deleted_node = current.next.value
        current.next = None  # Remove the last node
        return deleted_node

    def delete_at_front(self):
        """Delete the node at the front of the list and return its value."""
        if not self.head:  # If the list is empty
            return None
        deleted_node = self.head.value
        self.head = self.head.next  # Update the head to the next node
        return deleted_node
    
    def search(self, value):
        """Search for a node with the given value and return its index. Return 'Not Found!' if not present."""
        index = 0
        current = self.head
        while current:
            if current.value == value:  # If the value is found
                return index
            index += 1
            current = current.next
        return 'Not Found!'  # Value is not found

    def clear(self):
        """Clear the entire list."""
        self.head = None  # Reset head to None

    def size(self):
        """Return the number of nodes in the list."""
        num = 0
        current = self.head
        while current:
            num += 1  # Increment count for each node
            current = current.next
        return num

    def print_forward(self):
        """Print the values in the list from front to back."""
        current = self.head
        while current:
            print(current.value, end=' ')  # Print each value
            current = current.next
        print()  # For a new line after printing all values

    def print_backward(self):
        """Print the values in the list from back to front."""
        stack = []
        current = self.head
        while current:
            stack.append(current.value)  # Use a stack to reverse the order
            current = current.next
        while stack:
            print(stack.pop(), end=' ')  # Print values from the stack
        print()  # For a new line after printing all values

    def reverse_non_recursive(self):
        """Reverse the list non-recursively."""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Store the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev to current node
            current = next_node  # Move to the next node
        self.head = prev  # Update head to the new front

# Example usage of LinkedList class
my_list = LinkedList()
my_list.insert_in_back(10)
my_list.insert_in_back(20)
my_list.insert_in_back(30)
my_list.insert_in_front(5)
my_list.print_forward()  # Output: 5 10 20 30
my_list.delete_at_back()
my_list.print_forward()  # Output: 5 10 20
my_list.delete_at_front()
my_list.print_forward()  # Output: 10 20
print("Size of the list:", my_list.size())  # Output: Size of the list: 2
print("Search for value 10:", my_list.search(10))  # Output: Search for value 10: 0
print("Search for value 15:", my_list.search(15))  # Output: Search for value 15: Not Found!
my_list.reverse_non_recursive()
my_list.print_forward()  # Output: 20 10
