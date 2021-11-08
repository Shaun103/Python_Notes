# # last in first out # #   
# similar to an array as 
# the oldest thing in a stack is on the bottom


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)




s = Stack()

s.isEmpty()

s.push(1)

s.push('two')

s.push(True)

s.pop() # 1 - poped off

s.pop() # 'two' - poped off

s.pop() # True - popped off 

# print(s.peek()) # cant peek if all items removed

x = s.isEmpty()
print(x)