# -*- coding: utf-8 -*-
"""
Basic Password Bank
"""

pwd= input('What is the master password?')

def view():
    pass

def add():
    pass

while True:
    mode = input("ADD a new password or VIEW existing password(s) (add,view), press q to quit?").lower()
    if mode == 'q':
        break
        
    if mode == 'view':
        pass
    elif mode == 'add':
        pass
    else:
        print('Invalid Input.')
        continue