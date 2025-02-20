class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Pop an item from the stack."""
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped: {item}")
            return item
        print("Stack is empty!")
        return None

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        print("Stack is empty!")
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def display(self):
        """Display the current stack."""
        print("Stack:", self.stack)


# Example usage
if __name__ == "__main__":
    s = Stack()
    
    s.push(15)
    s.push(20)
    s.push(25)
    
    s.display()
    
    print("Top item:", s.peek())
    
    s.pop()
    s.display()

    print("Stack size:", s.size())
