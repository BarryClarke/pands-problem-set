#Program to sum all numbers between 1 and a positive integer inputted by the user
#Barry Clarke 22nd Jan 2019
#Rev1 - Operation to include erroneous entries

#Reference: https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
while True:
    try:
        i = int(input("Please enter a positive integer: "))
        n = i
        if i < 0:                                           # In the event of a negative integer being inputted by the user
            print("\nError: This is a negative integer")
            continue 
        else:
            Total = 0
            while i >= 0:
                Total = Total + i
                i = i - 1
            print("\nThe Sum of all positive integers up to", n , "is", Total)
        break                                               # breaks from the loop as this is the line where the program ends and reaches a result
    except ValueError:                                      # Used in the case of any non-integer inputted by the user
        print("\nError: This entry is not a positive integer") 