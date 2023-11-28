from deque import Deque
import random

#Takes response models from a file and puts them in a deque

class ResponseDatabase():
    def __init__(self, file):
        if type(file) == str:
            file = open(file, 'r')
        self.database = Deque()
        self.f = file
        
    def reader(self):
        
        for line in self.f:
            rand = random.randrange(1,10,1) #using random numbers to make the database have different order for the response models in every conversation
            line = self.f.readline()
            if rand % 2 == 0:
                self.database.add_right(line)
            elif rand % 2 == 1:
                self.database.add_left(line)
        self.f.close()
            
    def close(self):
        self.f.close()