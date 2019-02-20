#Program to sum all numbers between 1 and a positive integer inputted by the user
#Barry Clarke 18th Jan 2019
#Rev0 - Basic operation 

i = int(input("Please enter a positive integer: "))

if i < 0:
      i = int(input("This is a negative integer. Please enter a positive integer: "))

Sum = 0

while i >= 0:
   Sum = Sum + i
   i = i - 1
print(Sum)
