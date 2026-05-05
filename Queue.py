from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()

    def add(self, x):
        self.q.append(x)

    def safe_dequeue(self):
        if len(self.q) == 0:
            print("Queue is empty, cannot dequeue.")
        else:
            return self.q.popleft()

q = Queue()
q.add(10)
print(q.safe_dequeue())
print(q.safe_dequeue())