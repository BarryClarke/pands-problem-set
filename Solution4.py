#Program to recieve a positive integer and print all the numbers in sequence according to the Collatz conjecture
#Barry Clarke 25th Feb 2019
#Rev0 - Initial Revision

i = int(input("Please input a positive integer:\n"))

#Reference: https://stackoverflow.com/questions/26198131/check-if-input-is-positive-integer
while i != 1:                                               # 
    try:
        if i <= 0:                                          # In the event of a negative integer being inputted by the user
            print("\nThis is not a positive integer. Please enter a POSITIVE integer: ")
            break
        elif i % 2 == 0:                                    # If value is even
            i = i/2
            print(i)
            continue
        else:                                               # if value is odd
            i = (i*3) + 1
            print(i)
            continue
    except ValueError:                                     # Used in the case of any non-integer inputted by the user
        print("\nError: This entry is not a positive integer. Please enter only a POSITIVE INTEGER: ")
