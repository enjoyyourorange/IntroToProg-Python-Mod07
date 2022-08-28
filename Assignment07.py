import pickle
import re

n_dic={}
n_lst=[]




##########################################################################
#PICKLE PARTY


def add_to_pickle(name, a_lst):
    row={"Name": name}
    a_lst.append(row)
    return a_lst

def save_to_pickle(pickle_file, a_lst):
    with open ("name_libr.dat", 'ab') as pickle_file:
        pickle.dump(a_lst, pickle_file)
        pickle_file.close()

def read_from_pickle(pickle_file):
    with open ('name_libr.dat', 'rb') as pickle_file:
        pickle_return=pickle.load(pickle_file)
        print (pickle_return)

def load_all_pickle(pickle_file):
    with open (pickle_file, 'rb') as f:
        unpickled=[]
        while True:
            try:
                unpickled.append(pickle.load(f))
            except EOFError: #function is telling the program so continuously loop through the pickle file and load everything until it reaches the end
                break
    print (unpickled)

########################
# Menu Stuff

def user_menu():   
        """
        Show user the menu
        """
        print('''
        
        This is the name library, please select an option below:
        
        1: Enter a new name
        2. View previous names
        3. Exit
        
        ''')
        print()

def user_choice():
    while (True):
        question = (input("Please select a number from the above:   " "\n"))
        try:
            question=int(question) #make sure input is of an integer type
        except ValueError:
            print("\n""Integers only, no characters yet.""\n")
            break
        if question > 3:
            print(("\n""Value too high, try again.""\n"))
        if question <= 0:
            print("\n""Value too low, try again.""\n")
        else:
            return question

def user_entry():
    while (True):
        name = input("\n" "Please enter a name or list of characters here:   " "\n")
        if not re.match("^[a-z]*$", name, re.IGNORECASE): #use re module to make sure characters are being entered, not numbers. Ignoring any case values.
            print("\n" "Letters or characters only, please!""\n")
            break
        else:
            add_to_pickle(name,n_lst)
            save_to_pickle(name,n_lst)
            print ("\n" "Thanks, data has been saved.""\n")
            break

########################
# Main script
while (True):
    user_menu()
    int_entry=user_choice()
    if int_entry==1:
        user_entry()
    if int_entry==2:
        load_all_pickle("name_libr.dat")
    if int_entry==3:
        break