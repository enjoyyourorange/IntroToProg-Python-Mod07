import pickle
import re

n_dic={}
n_lst=[]
n_entry=""




##########################################################################
#PICKLE PARTY


def add_to_pickle(name, a_lst):
    row={"Name": name}
    a_lst.append(row)
    return a_lst

def save_to_pickle(pickle_file, a_lst):
    with open ("name_lib.dat", 'ab') as pickle_file:
        pickle.dump(a_lst, pickle_file)
        pickle_file.close()

def read_from_pickle(pickle_file):
    with open ('name_lib.dat', 'rb') as pickle_file:
        pickle_return=pickle.load(pickle_file)
        print (pickle_return)

def load_all_pickle(pickle_file):
    with open (pickle_file, 'rb') as f:
        unpickled=[]
        while True:
            try:
                unpickled.append(pickle.load(f))
            except EOFError:
                break
    print (unpickled)

########################
# Menu Shit

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
        question = (input("Please select a number from the above:   "))
        try:
            question=int(question)
        except ValueError:
            print("Integers only, no characters yet.")
            break
        if question > 3:
            print(("Value too high, try again."))
        if question <= 0:
            print("Value too low, try again.")
        else:
            return question



while (True):
    user_menu()
    int_entry=user_choice()

    if int_entry==1:
        name = input("Please enter a name or list of characters here:   " )
        if not re.match("^[a-z]*$", name):
            print ("Letter's only please.")
        add_to_pickle(name, n_lst)
        save_to_pickle(name, n_lst)
    if int_entry==2:
        load_all_pickle("name_lib.dat")
    if int_entry==3:
        break
 

