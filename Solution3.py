# Program to print all numbers between 1000 and 10000 that are divisible by 6 but not by 12
# Barry Clarke 1st Mar 2019
# Rev1 - Updated the spacing on indent from 6 spaces to 4

i = 1000

# Double while loop cuts down the calculations required, improving efficiency
# 1st while loop finds the first number >= 1000 that is disvisible by 6
while i <= 1006:
    if i % 6 != 0:
        i = i + 1
    else:
# 2nd while loop checks if number is divisible by 12, then adds 6 to this number
        while i <= 10000:
            if i % 12 != 0:
                print(i)
            i = i + 6

        
    