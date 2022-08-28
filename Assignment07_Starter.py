import pickle
import re

n_dic={}
n_lst=[]
n_entry=""




##########################################################################
#PICKLE PARTY


def add_to_pickle(name, a_lst):
    TODO#: ADD CODE HERE TO ADD NEW ENTRIES TO PICKLE FILE

def save_to_pickle(pickle_file, a_lst):
    TODO#: ADD CODE HERE TO SAVE ENTRIES TO PICKLE FILE


def read_from_pickle(pickle_file):
    TODO #: ADD CODE HERE TO READ FROM PICKLE FILE


def load_all_pickle(pickle_file):
    TODO#: ADD CODE HERE TO LOAD EVERY PREVIOUS ENTRY FROM PICKLE FILE

########################
# Menu 

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
        TODO#: ADD CODE HERE TO RESTRICT USER FROM ENTERING ANYTHING EXCEPT OUR MENU OPTIONS



########################
 # Main Script

while (True):
    TODO#: ADD CODE HERE TO TAKE USER INPUT AND REFLECT THAT OPTION. ALSO RESTRICT USER FROM ENTERING ANYTHING BUT CHARACTERS INTO THE NAME ENTRY.
    user_menu()
    int_entry=user_choice()
    TODO#: ADD CODE HERE TO RESTRICT USER FROM ENTERING ANYTHING EXCEPT OUR MENU OPTIONS
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
 

