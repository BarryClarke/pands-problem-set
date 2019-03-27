# Program that prints out the approximate square root of a floating point number
# Barry Clarke 26th Mar 2019
# Rev1 - Updated to improve the output response  


while True:
    try:
        f = float(input("Please enter a floating point number: "))
        break
    except ValueError:                                     
        print("\nError: This entry is not a floating point number") 


sqrt = f**(.5)
if f%(sqrt*sqrt) == 0:                                                      # If square root is perfect is a whole number
    print(f"The Square root of {f} is {sqrt}")
else:                                                                       # If square root is not a whole number and needs approximation                                                    
    print("The Square root of",f, "is approximately", format(sqrt, '.1f'))  #ref https://docs.python.org/3/tutorial/floatingpoint.html for printing a number with limited decimal places

