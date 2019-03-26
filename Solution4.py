# Program to recieve a positive integer and print all the numbers in sequence according to the Collatz conjecture
# Barry Clarke 1st Mar 2019
# Rev2 - Updated to have the positive integer check seperate from computation 

# Reference: https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
# While loop to verify that an inputted variable is a positive integer
while True:
    try:
        i = int(input("Please enter a positive integer: "))                                   
        if i < 1:                                 # In the event of a negative integer being inputted by the user
            print("\nError: This is not a positive integer")
            continue 
        else:
            break                                 # breaks from the loop as this is the line where the program ends and reaches a result
    except ValueError:                            # Used in the case of any non-integer inputted by the user
        print("\nError: This entry is not a positive integer") 

print(i, end=" ")                                 # https://stackoverflow.com/questions/ple-prints-on-the-same-line
while i != 1:
    if i % 2 == 0:                                # If value is even
        i = i//2 
        print(i, end=" ")                         # // returns an integer when using division (/ returns a float)
    else:
        i = (i*3) + 1
        print(i, end=" ")
print()                                           # Prints an empty line after all calculations are completed