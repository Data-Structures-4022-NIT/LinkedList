class Node:
    def __init__(self,value ):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_in_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def insert_in_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

        self.size += 1

    def delete_at_front(self):
        if self.head is None:
            return None
        delete_value = self.head.data
        self.head = self.head.next
        return delete_value

    def delete_at_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            remove_value = self.head.data
            self.head = None
            return remove_value
        while self.head.next.next is not None:
            self.head = self.head.next
        remove_value =self.head.next.data
        self.head.next = None
        return remove_value

    def search(self, value):
        index = 0
        while self.head is not None:
            if self.head.data == value:
                return index
            index += 1
            self.head = self.head.next
        return -1

    def clear(self):
        self.head = None
        self.size=0

    def size(self):
        count = 0
        while self.head is not None:
            count += 1
            self.head = self.head.next
        return count

    def print_forward(self):
        result = []
        while self.head is not None:
            result.append(str(self.head.data))
            self.head = self.head.next
        print(" ".join(result))

    def print_backward(self):
        result = []
        while self.head is not None:
            result.append(str(self.head.data))
            self.head = self.head.next
        print(result[::-1])

    def reverse_recursive(self, current=None, prev=None):
        if self.head is None:
            return

        if current is None:
            current = self.head

        if current.next is None:
            self.head = current
            current.next = prev
            return

        next_node = current.next
        current.next = prev
        self.reverse_recursive(next_node, current)

    def reverse_non_recursive(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
class Doublinklist:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        new_node = Doublinklist(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_in_back(self, value):
        new_node = Doublinklist(value)
        if self.head is None:
            self.head = new_node
            return
        while self.head is not None:
            self.head = self.head.next
        self.head.next = new_node
        new_node.prev = self.head

    def delete_at_front(self):
        if self.head is None:
            return None
        remove_value = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        return remove_value

    def delete_at_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            remove_value = self.head.data
            self.head = None
            return remove_value
        while self.head.next is not None:
            self.head = self.head.next
        remove_value =self.head.data
        self.head.prev.next = None
        return remove_value

    def search(self, value):
        index = 0
        while self.head is not None:
            if self.head.data == value:
                return index
            index += 1
            self.head = self.head.next
        return -1

    def clear(self):
        self.head = None
        self.size=0

    def size(self):
        count = 0
        while self.head is not None:
            count += 1
            self.head  =self.head.next
        return count

    def print_forward(self):
        result = []
        while self.head is not None:
            result.append(str(self.head.data))
            self.head = self.head.next
        print(" ".join(result))

    def print_backward(self):
        result = []
        while self.head is not None:
            result.append(str(self.head.data))
            self.head = self.head.next
        print(result[::-1])

    def reverse_recursive(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, node):
        if node is None or node.next is None:
            return node
        new_head = self._reverse_recursive(node.next)
        node.next.next = node
        node.next = None
        return new_head

    def reverse_non_recursive(self):
        prev = None
        curr = self.head
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def make_doubly(self, singlinked_list):
        if singlinked_list.head is None:
            return
        self.head = Doublinklist(singlinked_list.head.data)
        while singlinked_list.head.next is not None:
            new_node = Doublinklist(singlinked_list.head.next.data)
            self.head.next = new_node
            new_node.prev = self.head
            self.head = new_node
            singlinked_list = singlinked_list.next

    def shift(self, num):
        if self.head is None or num == 0:
            return
        size = self.size()
        num %= size
        if num < 0:
            num += size
        for i in range(num):
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = self.head
            self.head.prev = last_node
            self.head = self.head.next
            self.head.prev = None
            last_node.next = None

