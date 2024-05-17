class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = DoublyNode(data)
        if not self.head:
            self.head = newNode
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
        newNode.prev = lastNode

    # insert in front
    def prepend(self, data):
        newNode = DoublyNode(data)
        if self.head:
            self.head.prev = newNode
            newNode.next = self.head
        self.head = newNode

    def display(self):
        if not self.head:
            print("The linked list is empty.")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

    def delete_at_front(self):
        if not self.head:
            print("LinkedList is empty")
            return
        deletedValue = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        print(deletedValue)

    def delete_at_back(self):
        if not self.head:
            print('LinkedList is empty')
            return
        if self.head.next is None:
            deletedValue = self.head.data
            self.head = None
            print(deletedValue)
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        deletedValue = lastNode.data
        lastNode.prev.next = None
        print(deletedValue)

    def search(self, value):
        if not self.head:
            print("LinkedList is empty")
            return
        current = self.head
        position = 0
        while current:
            if current.data == value:
                print(f"list.search({value}) -> {position}")
                return
            current = current.next
            position += 1
        print("nothing found")

    def clear(self):
        self.head = None
        print("LinkedList cleared")

    def size(self):
        if not self.head:
            print("LinkedList is empty")
            return
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        print(f"LinkedListSize() -> {count}")

    def print_forward(self):
        if not self.head:
            print("LinkedList is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_backward(self):
        if not self.head:
            print("LinkedList is empty")
            return
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

    def reverse_non_recursively(self):
        if not self.head:
            print("LinkedList is empty")
            return
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def shift(self, num):
        if not self.head:
            print("LinkedList is empty")
            return
        if num == 0:
            return
        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1
        current.next = self.head
        self.head.prev = current
        num %= length
        for _ in range(length - num):
            self.head = self.head.next
        current = self.head.prev
        current.next = None
        self.head.prev = None


# make the singleLinkedList to doublyLinkedList
def make_doubly(singly_linked_list):
    doubly_linked_list = DoublyLinkedList()
    current = singly_linked_list.head
    while current:
        doubly_linked_list.append(current.data)
        current = current.next
    return doubly_linked_list


# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(10)
dll.prepend(25)
dll.display()
dll.delete_at_front()
dll.delete_at_back()
dll.search(10)
dll.size()
dll.print_forward()
dll.print_backward()
dll.reverse_non_recursively()
dll.display()
dll.clear()
dll.display()
