class StackQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    # Stack Operations
    def push_to_stack(self, value):
        self.stack.append(value)

    def pop_from_stack(self):
        if not self.is_stack_empty():
            return self.stack.pop()
        raise IndexError("Stack is empty.")

    def peek_stack(self):
        if not self.is_stack_empty():
            return self.stack[-1]
        raise IndexError("Stack is empty.")

    def is_stack_empty(self):
        return len(self.stack) == 0

    # Queue Operations
    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_queue_empty():
            return self.queue.pop(0)
        raise IndexError("Queue is empty.")

    def is_queue_empty(self):
        return len(self.queue) == 0

    # Example Usage
    def stack_example(self):
        print("Stack Example:")
        self.push_to_stack(10)
        self.push_to_stack(20)
        print(f"Stack after pushing: {self.stack}")  # [10, 20]
        print(f"Popped from stack: {self.pop_from_stack()}")  # 20
        print(f"Stack after popping: {self.stack}")  # [10]

    def queue_example(self):
        print("Queue Example:")
        self.enqueue(10)
        self.enqueue(20)
        print(f"Queue after enqueue: {self.queue}")  # [10, 20]
        print(f"Dequeued from queue: {self.dequeue()}")  # 10
        print(f"Queue after dequeue: {self.queue}")  # [20]

sq = StackQueue()
sq.stack_example()
sq.queue_example()
