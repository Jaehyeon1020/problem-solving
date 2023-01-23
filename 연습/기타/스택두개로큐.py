class StackQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, data):
        self.input_stack.append(data)

    def dequeue(self):
        if self.output_stack:
            return self.output_stack.pop()
        else:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

            return self.output_stack.pop()


q = StackQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.input_stack)
print(q.output_stack)
