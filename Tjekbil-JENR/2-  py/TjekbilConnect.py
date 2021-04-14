# Function in separate file to be included (using import) whenever you need it
# April 2021, jenr@kea.dk
# Used in KEA BE-IT 2nd semester SC, module 5, day 5

import mysql.connector

def dbconnect():
	connection = mysql.connector.connect(
	    host = 'localhost',
	    database = 'Tjekbil',
	    user = 'root',
	    password = '7890/()='
	)
	return connection
