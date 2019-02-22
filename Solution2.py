#Program to check if today starts with a T
#Barry Clarke 22nd Jan 2019
#Rev0 - Basic operation 

import datetime

#Referenced example from week 2 leactures
if (datetime.datetime.today().weekday() == 1) or (datetime.datetime.today().weekday() == 3):
      print("Today begins with a T")
else:
      print("Today does not begin with a T")


