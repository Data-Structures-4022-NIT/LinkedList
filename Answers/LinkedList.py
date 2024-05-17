class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert in back
    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    # insert in front
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_after(self, prev_node_data, data):
        if not self.head:
            print("The linked list is empty.")
            return
        currentNode = self.head
        while currentNode:
            if currentNode.data == prev_node_data:
                new_node = Node(data)
                new_node.next = currentNode.next
                currentNode.next = new_node
                return
            currentNode = currentNode.next
        print(f"{prev_node_data} not found in the linked list.")

    def delete(self, data):
        if not self.head:
            print("The linked list is empty.")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prevNode = self.head
        currentNode = self.head.next
        while currentNode:
            if currentNode.data == data:
                prevNode.next = currentNode.next
                return
            prevNode = currentNode
            currentNode = currentNode.next
        print(f"{data} not found in the linked list.")

    def display(self):
        if not self.head:
            print("The linked list is empty.")
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

    def delete_at_front(self):
        if self.head == None:
            print("LinkedList is empty")

        else:
            deletedValue = self.head.data
            self.head = self.head.next
            print(deletedValue)

    def delete_at_back(self):
        if self.head == None:
            print('LinkedList is empty')

        # If there is only one node
        if self.head.next == None:
            deletedValue = self.head.data
            self.head = None
            print(deletedValue)
        lastElement = self.head
        while lastElement.next.next:
            prevLastElement = lastElement
            lastElement = lastElement.next
        deletedValue = lastElement.next.data
        lastElement.next = None
        print(deletedValue)

    def search(self, value):
        if self.head == None:
            print("LinkedList is empty")
        current = self.head
        position = 0
        while current:
            if current.data == value:
                print(f"list.search({value}) -> {position}")
            current = current.next
            position += 1
        print("nothing found")

    def clear(self):
        if self.head == None:
            print("LinkedList is empty")
        self.head = None
        print("LinkedList cleared")

    def size(self):
        if self.head == None:
            print("LinkedList is empty")
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        print(f"LinkedListSize()-> ({count})")

    def print_forward(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        self._print_backward_recursive(self.head)
        print()

    def _print_backward_recursive(self, node):
        if node.next:
            self._print_backward_recursive(node.next)
        print(node.data, end=" ")

    def reverse_recursive(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        self.head = self._reverse_recursively(self.head)

    def _reverse_recursively(self, current):
        if current.next == None:
            return current
        new_head = self._reverse_recursively(current.next)
        current.next.next = current
        current.next = None
        return new_head

    def reverse_non_recursively(self):
        if self.head == None:
            print("LinkedList is empty")
            return
        prevNode = None
        currentNode = self.head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode


# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(25)
ll.prepend(10)
ll.display()
ll.delete_at_front()

ll.delete_at_back()

ll.search(10)
ll.size()
ll.print_forward()
ll.reverse_non_recursively()
ll.display()
ll.clear()
ll.display()
