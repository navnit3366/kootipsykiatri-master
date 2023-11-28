from input import Input

class DebugMode():
    def __init__(self):
        self.database = Input.database
        #self.key = Input.find_key
        
    def read(self):
        while self.database.is_empty() == False:
            print(self.database.read_left())
        print("/nkey:  ")
        #print(self.key)