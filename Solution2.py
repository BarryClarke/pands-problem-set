# Program to check if today starts with a T
# Barry Clarke 24th Feb 2019
# Rev2 - Updated the spacing on indent from 6 spaces to 4

import datetime

# How to identify a specific part of the imported datetime: https://www.pythonforbeginners.com/basics/python-datetime-time-examples
Day = datetime.date.today().strftime("%A")
print("Today is", Day)

if Day[0] == "T":
    print("Today begins with a T")
else:
    print("Today does not begin with a T")


