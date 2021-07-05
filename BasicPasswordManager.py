"""

Basic Password Bank

*Need pip install cryptography

"""

#module to encrpyt text
from cryptography.fernet import Fernet

#Functions:
    
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            #rstrip removes the \n from the add
            data = line.rstrip()
            #user is 0 index, passw is 1 index
            user, passw = data.split('|')
            print("User:", user, '|| Password:', passw)
    
def add():
    name = input('Account Name:\n')
    pwd = input("Password:\n")
    
    #with will manually close the txt file a = append, r = read, w = write
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n' )


#Program:
    
master_pwd= input('What is the master password?\n')
key = load_key() + master_pwd.bytes
fer = Fernet(key)
    
while True:
    mode = input("ADD a new password or VIEW existing password(s) (add,view), press q to quit?\n").lower()
    if mode == 'q':
        break
        
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Input.')
        continue