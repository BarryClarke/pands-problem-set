#Program to sum all numbers between 1 and a positive integer inputted by the user
#Barry Clarke 1st Mar 2019
#Rev2 - Updated to have the positive integer check seperate from computation

#Reference: https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
# While loop to verify that an inputted variable is a positive integer
while True:
    try:
        i = int(input("Please enter a positive integer: "))
        if i < 1:                                           # In the case of a negative integer being inputted by the user
            print("\nError: This is not a positive integer")
            continue 
        else:
            break                                           # breaks from the loop as this is the line where the program ends and reaches a result
    except ValueError:                                      # In the case of any non-integer inputted by the user
        print("\nError: This entry is not a positive integer") 

# Once input is verified to be a positive integer, computation of the sum be done
n = i
Total = 0
while i >= 0:
    Total = Total + i
    i = i - 1
print("\nThe Sum of all positive integers up to", n , "is", Total)