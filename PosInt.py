# A program to verify if an inputted variable is an integer

# While loop to verify that an inputted variable is a positive integer
while True:
    try:
        i = int(input("Please enter a positive integer: "))
        if i < 0:                                           # In the case of a negative integer being inputted by the user
            print("\nError: This is a negative integer")
            continue 
        else:
            break                                           # breaks from the loop as this is the line where the program ends and reaches a result
    except ValueError:                                      # In the case of any non-integer inputted by the user
        print("\nError: This entry is not a positive integer") 


print("\nThis is indeed a positive integer")
