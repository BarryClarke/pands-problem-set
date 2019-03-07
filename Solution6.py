# Program that prints out every second word of an inputted string
# Barry Clarke 7th Mar 2019
# Rev0 - Initial Revision

Sentence = str(input("Please enter a sentence\n"))

Word_list = Sentence.split()                    # Reference https://stackoverflow.com/questions/41228115/how-to-extract-the-first-and-final-words-from-a-string

for i in range(0,len(Word_list),2):             # Reference https://docs.python.org/3/tutorial/controlflow.html#the-range-function
    print(Word_list[i], end=" ")                # end=" " keeps each word on the same line with a space between them
print()





