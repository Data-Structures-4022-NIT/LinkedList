class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_in_back(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_front(self):
        if not self.head:
            return None
        deleted_node = self.head.value
        self.head = self.head.next
        return deleted_node

    def delete_at_back(self):
        if not self.head:
            return None
        if not self.head.next:
            deleted_node = self.head.value
            self.head = None
            return deleted_node
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next.value
        current.next = None
        return deleted_node

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
        stack = []
        current = self.head
        while current:
            stack.append(current.value)
            current = current.next

        while stack:
            print(stack.pop(), end=' ')

    def reverse_non_recursive(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


my_list = LinkedList()
my_list.insert_in_front(3)
my_list.insert_in_front(2)
my_list.insert_in_front(1)
my_list.print_forward()
