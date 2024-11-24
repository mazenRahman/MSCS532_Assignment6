class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a value at the end
    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node by value
    def delete(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next

    # Traverse the list
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # Example Usage
    def example(self):
        print("Singly Linked List Example:")
        self.insert(10)
        self.insert(20)
        self.insert(30)
        print("After Insertions:")
        self.traverse()  # 10 -> 20 -> 30 -> None

        self.delete(20)
        print("After Deleting 20:")
        self.traverse()  # 10 -> 30 -> None

linked_list = SinglyLinkedList()
linked_list.example()
