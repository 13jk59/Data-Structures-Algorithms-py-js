class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None 

class Stack:
    def __init__(self, val):
        self.head = StackNode(val)
        self.tail = self.head 
    
    def push(self,val):
        new_node = StackNode(val)
        self.tail.next = new_node
        new_node.prev = self.tail 
        self.tail = new_node

    def pop(self):
        if self.tail:
            new_tail = self.tail.prev
            old_tail_val = self.tail.val 
            new_tail.next = None
            self.tail = new_tail 
            return old_tail_val
    
    def top(self):
        if self.tail:
            return self.tail.val
    
    