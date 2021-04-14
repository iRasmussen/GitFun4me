# My first stab at a vehicle lookup service
# April 2021, jenr@kea.dk
#
# We import modules here
import os
import TjekbilConnect as tbc

# Connect to database
tbc.dbconnect()
# Disconnect
tbc.close()

def clearTerminal():
    # No input parameters, requires os module
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcomeMsg():
    print(50*'-')
    print('Welcome to Tjekbil - JENR edition')

def showDbInfo():
    print('Den er fin!')

def menu(choiceDict):
    while True:
        print('+------+\n+ Menu +\n+------+')
        print(choiceDict)
        print('Type Q to quit')
        print(20*'-')
        msg = input('->')
        if msg.upper() == 'Q':
            print('Thanks for using Tjekbil - goodbye')
            break
        elif msg == '1':
            showDbInfo()
        else:
            print('Please select a valid menu choice')

# Set up available menu choices
choiceDict = {1:'Show database info'}

clearTerminal()
welcomeMsg()
menu(choiceDict)
