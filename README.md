# LinkedList

## SinglyLinkedList

Create a LinkedList that has the following functions

### 1. insert_in_front(value)

This function takes a value and add it in front of the LikedList

list -> [1, 2, 3]

list.insert_in_front(10)

list -> [10, 1, 2, 3]

### 2. insert_in_back(value)

This function takes a value and add it at the end of the LikedList

list -> [1, 2, 3]

list.insert_in_back(10)

list -> [1, 2, 3, 10]

### 3. delete_at_front()

This function deletes the first value of the LikedList and returns it

list -> [1, 2, 3]

list.delete_at_front() -> 1

list -> [2, 3]

### 4. delete_at_back()

This function deletes the last value of the LikedList and returns it

list -> [1, 2, 3]

list.delete_at_back() -> 3

list -> [1, 2]

### 5. search(value)

This function returns the index of the first element with the corresponding value

list -> [1, 3, 2, 2]

list.search(1) -> 0

list.search(2) -> 2

### 6. clear()

This function clears the LinkedList

list -> [1, 2, 3, 4]

list.clear()

list -> []

### 7. size()

This function returns the number of elements in the LinkedList

list -> [1, 2, 3]

list.size() -> 3

### 8. print_forward()

prints all the elements from start to end

list -> [1, 2, 3]

list.print_forward() -> "1 2 3"

### 9. print_backward()

prints all the elements from end to start

list -> [1, 2, 3]

list.print_backward() -> "3 2 1"

### 10. reverse_recursive()

reverse the LinkedList recursively

list -> [1, 2, 3]

list.reverse_recursive()

list -> [3, 2, 1]

### 11. reverse_non_recursive()

reverse the LinkedList non-recursively

list -> [1, 2, 3]

list.reverse_non_recursive()

list -> [3, 2, 1]

## DoublyLinkedList

### Create a DoublyLinkedList with above functions (same as SinglyLinkedList)

### make_doubly(SinglyLinkedList)

This function takes a SinglyLinledList and turns it into a DoublyLinkedList

### shift(num)

shift all elements forward according to num

list -> [1, 2, 3, 4, 5]

list.shift(2)

list -> [4, 5, 1, 2, 3]

---

list -> [1, 2, 3, 4, 5]

list.shift(-1)

list -> [2, 3, 4, 5, 1]
