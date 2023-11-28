from response import Response
from reader import Reader
from input import Input
#from debug-mode import DebugMode
from conversation import Conversation



def main():
    
    conversation = Conversation("conversation.txt") #saves the current conversation
    conversation.f.write("turhaaaaaaaa\n")
    inputt = Input() #takes the users inputs
    response = Response("blaa") #creates a response according to input
    
    print("I am your personal home psychiatrist. I can help with any problems you have.\n")
    choice = input("What do you want to do today? Write either 1, 2 or 3.\n\n1. Psychiatrist appointment\n2. Read saved appointments\n3. Exit home psychiatrist\n")
    
    while choice != '3':
        if type("files.txt") == str: #Tries to open file with the given name
            files = open("files.txt", 'a')
        
        if choice == '1':
            inputt.u_input = input("Hello and welcome to my office. Tell me what can I help you with. What is on your mind?\n")
            conversation.k_response = "Hello and welcome to my office. Tell me what can I help you with. What is on your mind?"
            conversation.u_input = inputt.u_input
            inputt.database.add_right(inputt.u_input)
            
            while choice == '1': #conversation with the psychiatrist
                conversation.save()
                
                if 'goodbye' in inputt.u_input.lower():
                    print("Goodbye, I hope to see you again. Take care!\n")
                    conversation.f.write("Psychiatrist:    " + "Goodbye, I hope to see you again. Take care!")
                    save_convo = input("Do you want to save this conversation?\n\n1. Save and exit\n2. Exit\n")
                    if save_convo == '1':
                        name = input("Give the conversation a name and .txt in the end.\n")
                        conversation.copy(name)
                        files.write(name + "\n\n")
                        break
                    else:
                        conversation.f.truncate(0) #empties the temporary file conversation.txt
                        break
                
                response.u_input = inputt.u_input
                response.find_key()
                response.create_response(inputt)
                conversation.k_response = response.response
                inputt.u_input = input(response.response + "\n")
                conversation.u_input = inputt.u_input
                inputt.database.add_right(inputt.u_input)
                
        files.close()
        while choice == '2': #reading old conversations
            if type("files.txt") == str: #Tries to open file with the given name
                files = open("files.txt", 'r')
            
            print("Which conversation would you like to view? Write the full name with the .txt extension.\n")
            line = files.readline()
            for line in files:
                print(line)
                line = files.readline()
            which_file = input()
            if type(which_file) == str: #Tries to open file with the given name
                view = open(which_file, 'r')
            line2 = view.readline()
            for line2 in view:
                print(line2)
                line2 = view.readline()
            answer = input("\nWould you like to continue reading conversations y/n.\n")
            if answer == 'y':
                continue
            elif answer == 'n':
                break
            
        files.close()
        choice = input("What do you want to do next?\n\n1. Another psychiatrist appointment\n2. Read saved appointments\n3. Exit home psychiatrist\n")
        
    conversation.f.close()
    print("Thank you for using home psychiatrist! See you next time!")
    
if __name__ == '__main__': 
    main()