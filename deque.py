import collections

class Deque():
    def __init__(self):
        self.deque = collections.deque()
        
    def add_right(self, string): #adds element to the right side of the deque
        self.deque.append(string)
        
    def add_left(self, string): #adds to the left side
        self.deque.appendleft(string)
        
    def pop_right(self): #takes an element from the right side of the deque and removes it
        return self.deque.pop()
    
    def pop_left(self): #takes an element from the left side and removes it
        return self.deque.popleft()
    
    def read_right(self): #takes an element from the right side, but doesn't remove it
        read = self.deque.pop()
        self.deque.append(read)
        return read
    
    def read_left(self): #takes an element from the left side, but doesn't remove it
        read = self.deque.popleft()
        self.deque.appendleft(read)
        return read
    
    def is_empty(self): #checks if the deque is empty and returns True if it is
        if self.deque:
            return False
        else:
            return True