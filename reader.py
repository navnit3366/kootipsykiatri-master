from conversation import Conversation

class Reader():
    def __init__(self, file):
        if type(file) == str: #Tries to open file with the given name
            file = open(file, 'r')
        self.f = file
        
    def read(self): #Reads the file with the given name
        for line in self.f:
            print(self.f.readline())
            
            
    def close(self):
        self.f.close()