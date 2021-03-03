# Script to determine whether it is Friday today
# 2021-03-03 jenr@kea.dk

# Import module to get date and time info
import datetime

# Put current date and time into var for easier writing
cdt = datetime.datetime.now()

# Begin with a line and a description
print(55*'-')
print('Is it Friday?')
print('We will tell you now!')
print(f"The year is {cdt.year}, that's for sure!")
# Weekday, full version, refer to https://www.w3schools.com/python/python_datetime.asp
weekday = cdt.strftime('%A')
if(weekday == 'Friday'):
    print("Yes, it's actually Friday!")
else:
    print("Oh darn, not yet, it's only {weekday}")
print('Thank you and goodbye...')
print(55*'-')
