from response_database import ResponseDatabase
import random

class Response():
    def __init__(self, input):
        self.database1 = ResponseDatabase("response_data1.txt") #has response model-sentences
        self.database1.reader() #reads the file into the deque
        
        self.database2 = ResponseDatabase("response_data2.txt") #has response model-sentences for user shouting
        self.database2.reader() #reads the file into the deque
        
        self.database3 = ResponseDatabase("response_data3.txt") #has response model-sentences for user's questions
        self.database3.reader() #reads the file into the deque
        
        self.database4 = ResponseDatabase("response_data4.txt") #has response model-sentences for user's questions
        self.database4.reader() #reads the file into the deque
        
        self.database5 = ResponseDatabase("response_data5.txt") #has response model-sentences for user's questions
        self.database5.reader() #reads the file into the deque
        
        self.u_input = input #User's latest input
        self.response = ""
        self.key = 1
        
    
    def find_key(self):
        self.key = 1 #no special key
        if '!' in self.u_input:
            self.key = 2
        if '?' in self.u_input:
            self.key = 3
        if 'I ' in self.u_input.lower():
            self.key = 4
        if 'my ' in self.u_input.lower():
            self.key = 5
        
    
    def create_response(self, input):
        if self.database1.database.is_empty() == True: #if all response models are used, database resets
            self.database1 = ResponseDatabase("response_data1.txt")
            self.database1.reader()
        
        if self.database2.database.is_empty() == True: #if all response models are used, database resets
            self.database2 = ResponseDatabase("response_data2.txt")
            self.database2.reader()
        
        if self.database3.database.is_empty() == True: #if all response models are used, database resets
            self.database3 = ResponseDatabase("response_data3.txt")
            self.database3.reader()
            
        if self.database4.database.is_empty() == True: #if all response models are used, database resets
            self.database4 = ResponseDatabase("response_data4.txt")
            self.database4.reader()
            
        if self.database5.database.is_empty() == True: #if all response models are used, database resets
            self.database5 = ResponseDatabase("response_data5.txt")
            self.database5.reader()
            
        
        
        
        rand = random.randrange(1,10,1) #more use of random numbers to make conversations seem unique           
        if self.key == 1: #regular responses
            if rand % 2 == 0:
                self.response = self.database1.database.pop_right().rstrip("\n")
            if rand % 2 == 1:
                self.response = self.database1.database.pop_left().rstrip("\n")
            if ',' in self.response: #commas mean that the response model uses the user's input
                self.response = self.response + self.u_input
        
        elif self.key == 2: #responses for uer inputs that have exclamation mark
            if rand % 2 == 0:
                self.response = self.database2.database.pop_right().rstrip("\n")
            if rand % 2 == 1:
                self.response = self.database2.database.pop_left().rstrip("\n")
            if ',' in self.response:
                self.response = self.response + input.database.pop_right()
        
        elif self.key == 3: #responses for questions
            if rand % 2 == 0:
                self.response = self.database3.database.pop_right().rstrip("\n")
            if rand % 2 == 1:
                self.response = self.database3.database.pop_left().rstrip("\n")
            if ',' in self.response:
                self.response = self.response + input.database.pop_right()
                
        elif self.key == 4: #I found in user input
            position = self.u_input.lower().find("i ") + 2
            if rand % 2 == 0:
                self.response = self.database4.database.pop_right().rstrip("\n") + "you " + self.u_input[position:]
            if rand % 2 == 1:
                self.response = self.database4.database.pop_left().rstrip("\n") + "you " + self.u_input[position:]
                
        elif self.key == 5: #my found in user input
            position = self.u_input.lower().find("my ") + 3
            if rand % 2 == 0:
                self.response = self.database5.database.pop_right().rstrip("\n") + "your " + self.u_input[position:]
            if rand % 2 == 1:
                self.response = self.database5.database.pop_left().rstrip("\n") + "your " + self.u_input[position:]