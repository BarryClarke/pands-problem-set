# Program that prints out the approximate square root of a floating point number
# Barry Clarke 12th Mar 2019
# Rev0 - Initial Revision


while True:
    try:
        f = float(input("Please enter a floating point number: "))
        break
    except ValueError:                                     
        print("\nError: This entry is not a floating point number") 


sqrt = f**(.5)                                                       
print("The Square root of",f,"is approximately", format(sqrt, '.1f')) #ref https://docs.python.org/3/tutorial/floatingpoint.html for printing a number with limited decimal places

