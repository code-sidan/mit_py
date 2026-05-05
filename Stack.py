class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def safe_pop(self):
        if len(self.s) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        return self.s.pop()

st = Stack()
st.push(1)
print(st.safe_pop())
print(st.safe_pop())