
# Program that reads in a User specified text file and outputs every second line of the file
# Barry Clarke 26th Mar 2019
# Rev0 - Initial Revision

import sys

if len(sys.argv) == 2:                              # Checks that the only one argurment is inputted by the user                             
    step = 2                                        # Reference https://stackoverflow.com/questions/47062493/how-can-i-get-python-to-read-every-nth-line-of-a-txt-file
    with open(sys.argv[1], 'r') as f:
        for lineno, line in enumerate(f):
            if lineno % step == 0:
                print(line, end="")           
else:
    print("You should supply a single filemname")