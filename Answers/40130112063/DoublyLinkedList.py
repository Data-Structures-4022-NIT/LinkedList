class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_in_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def insert_in_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def delete_at_front(self):
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
        if not self.head:
            return None
        if self.head == self.tail:
            deleted_node = self.head.value
            self.head = self.tail = None
            return deleted_node
        deleted_node = self.tail.vaule

    def search(self, value):
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next
        return 'Not Found!'

    def clear(self):
        self.head = None
        self.tail = None

    def size(self):
        num = 0
        current = self.head
        while current:
            num += 1
            current = current.next
        return num

    def print_forward(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next

    def print_backward(self):
        current = self.tail
        while current:
            print(current.value, end=' ')
            current = current.prev
        print('None')

    def reverse_non_recursive(self):
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

    def make_doubly(self, singly_list):
        doubly_list = DoublyLinkedList()
        if not singly_list.head:
            return 'The list is empty!'
        current = singly_list.head
        previous = None
        while current:
            current.prev = previous
            previous = current
            current = current.next

    
my_list = DoublyLinkedList()
my_list.insert_in_front(2)
my_list.insert_in_front(2)
my_list.insert_in_front(3)
my_list.insert_in_front(1)
