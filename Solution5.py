# Program to check in an inputted positive integer is a prime number
# Barry Clarke 2nd Mar 2019
# Rev1 - Updated rev to correct a apelling error on comments section

# Reference: https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
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

n = 2
x = i
while n < x:
    if i % n == 0:
        print(i,"is divisible by",n,"hence it is not a prime number")
        break
    else:
        x = i // n
        n = n + 1
else:
    print(i, "is a prime number")
    

    



