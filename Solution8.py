# Program that prints out today's date and time in a specifc format
# Barry Clarke 19th Mar 2019
# Rev0 - Initial Revision

# Using datetime module
import datetime                                                                             

# Ref https://docs.python.org/3/library/datetime.html for formatting
Time = datetime.datetime.strftime(datetime.datetime.now(), "%A, %B %d %Y at %I:%M%p")

print(Time)
