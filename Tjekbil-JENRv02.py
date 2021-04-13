# New version built upon https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# April 2021, jenr@kea.dk
#
# +++++++
# MODULES
# +++++++
# We import modules here
import os
import mysql.connector
from beautifultable import BeautifulTable

# ++++++++++++
# DICTIONARIES
# ++++++++++++
# Dictionary of database connection parameters, should be in config file
config = {
  'user': 'root',
  'password': '7890/()=',
  'host': 'localhost',
  'database': 'Tjekbil',
  'raise_on_warnings': True
}

# Dictionary of menu choices
choiceDict = {
    1 : 'Show database info',
    2 : 'Show license plates'
}

# Connect to database
cnx = mysql.connector.connect(**config)
# Define cursor
mc = cnx.cursor()

# +++++++++
# FUNCTIONS
# +++++++++
# functions that need to be defined before running via menu
def clearTerminal():
    # No input parameters, requires os module
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcomeMsg():
    print(50*'-')
    print('Welcome to Tjekbil - JENR edition')

def getInfo():
    i = cnx.get_server_info()
    if i == 'None':
        print('Connection not present, sorry!')
    else:
        print(f'Connected to MySQL version {i}, looking good.\n✔︎')

def displayTable(header, rows):
    # header must be a list of strings
    # rows must be a list of tuples
    table = BeautifulTable()
    table.set_style(BeautifulTable.STYLE_MARKDOWN)
    table.columns.header = header
    for row in rows:
        table.rows.append(row)
    print(table)

def showRowsInTable(query):
    # query must be a valid sql query string
    mc.execute(query)
    return mc.fetchall()

def showAll_a():
    # a simple query from one table
    q = """
        SELECT
            Number, Status
        FROM
            Licenseplate
    """
    tableHeader = ['Nummerplade', 'Status']
    tableRows = showRowsInTable(q)
    displayTable(tableHeader, tableRows)

def showAll_b():
    # a query from a view
    q = """
        SELECT
            *
        FROM
            VehicleReg
    """
    tableHeader = ['Number', 'Make', 'Model', 'Year']
    tableRows = showRowsInTable(q)
    displayTable(tableHeader, tableRows)
    # print(len(tableRows[0]))




def menu(choiceDict):
    while True:
        print()
        print('---\tMenu\t---')
        # print(choiceDict)
        for num, txt in choiceDict.items():
            print(f'{num} - {txt}')
        print('Type Q to quit')
        print(20*'-')
        msg = input('->')
        if msg.upper() == 'Q':
            print('Thanks for using Tjekbil.')
            break
        elif msg == '1':
            getInfo()
        elif msg == '2':
            showAll_b()
        else:
            print('Please enter a valid menu choice.')

# ++++++
# ACTION
# ++++++
# Now, we actually do things!
clearTerminal()
welcomeMsg()
menu(choiceDict)




# Disconnect
cnx.close()
