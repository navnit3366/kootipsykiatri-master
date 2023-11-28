import shutil
from input import Input
from response import Response
import time

class Conversation(): #Keeps track of the conversation and saves it to a file
    def __init__(self, file):
        if type(file) == str:
            file = open(file, 'r+')
        self.f = file
        self.u_input = ""
        self.k_response = ""
        
    def save(self): #saves the latest input and response to a temporary file
        self.f.write("Psychiatrist:    " + self.k_response + "\n\n")
        self.f.write("Patient:         " + self.u_input + "\n\n")
        
        
    def copy(self, newfile): #copies a conversation from the temporary file to a file with user's specified name
        self.f.close()
        if type("conversation.txt") == str:
            file = open("conversation.txt", 'r+')
        if type(newfile) == str:
            newfile = open(newfile, 'w')
        newfile.write("turhaaaa\n")
        newfile.write(time.strftime("%d/%m/%Y") + "\n\n")
        line = file.readline()
        for line in file:
            newfile.write(line + "\n")
            line = file.readline()
        file.truncate(0) #empties the temporary file
        
    def close(self):
        self.f.close()