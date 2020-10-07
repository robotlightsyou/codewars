import sys
if len(sys.argv) != 3:  # asks for a valid input
    print(f"Usage: python dna.py data.csv sequence.txt")
    exit(1)

''' unlike C, you don't have to declare everything at the top. I personally prefer to declare
things close to where they are implemented, but I'm honestly not sure what the PEP8 standard is.
I've adjusted things to fit my style, FWIW. '''
# defines all the variables
''' document_file = sys.argv[1]
dna_file = sys.argv[2]
text = open(dna_file)
people = open(document_file) '''

''' "open(file)" is almost always a sniff, instead use a context manager
https://www.youtube.com/watch?v=C-gEQdGVXbk&feature=emb_logo&t=4m25s '''

with open(sys.argv[2], newline='') as f:
    text = f.read()
with open(sys.argv[1], newline='') as f:
    people = f.read()

''' these are unused
temp_list = []
list_of_people = [] '''


''' letters = []
for words in text:  # makes a list of all the dna letters in the letters file
    for letter in words:
        letters.append(letter) '''

''' list comprehensions are normally more readable, but I'm not sure that is true when nesting like this.
I decided to leave it more for exposure than suggesting it's best practices.
I found the syntax here:
https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/ '''
letters = [letter for word in text for letter in word]

''' dna_list = []
for line in people:  # adds all of the sentences into a list
    dna_list.append(line) '''

dna_list = [line for line in people]

''' for i in range(len(dna_list)):  # makes the dna_list into a string
    peoples_dna += dna_list[i]
peoples_dna = peoples_dna.strip() '''

peoples_dna = ''
for _, val in enumerate(dna_list):  # makes the dna_list into a string
    peoples_dna += val
peoples_dna = peoples_dna.strip()

''' Don't overwrite reserved keywords like 'list', 'dict', 'str', it can have bad consequences
list = [] '''
'''lst = []
for sentence in peoples_dna.splitlines():  # makes a double list where there is few list in a list
    lst.append(sentence.split(',')) '''

lst = [sentence.split(',') for sentence in peoples_dna.splitlines()]


def get_repeat_list(letters=[]):

    dna_repeated_list = []
    for m in range(len(lst[0]) - 1):
        ''' by putting total_appear_time_list here you automatically reset it on each loop, meaning you don't
        have to do it manually at the end. The same applies for total_times '''
        total_appear_time_list = []
        m = m + 1
        # checks the number of times something appeared in the list
        for i in range(len(letters) - 3):
            total_appear_times = 0
            word = ""  # makes it go be nothing

            try:  # if it gets to the end of the dna line it will make a list of range not found
                ''' for a in range(len(lst[0][m])):

                    word += letters[a + i] '''
                for idx, _ in enumerate(lst[0][m]):

                    word += letters[idx + i]
            except:
                break
            while word == lst[0][m]:  # does it until the word is not the dna part

                total_appear_times += 1

                word = ''

                try:
                    i = i + len(lst[0][m])

                    for a in range(len(lst[0][m])):

                        word += letters[a + i]

                except:  # remember to check if there is a error 'list index out of range'
                    break  # exits the loop becuase it is at the end of the dna line
            # makes the number of repetion into a list
            total_appear_time_list.append(total_appear_times)

            ''' this sort is costing you a lot, and is unnecessary because of the max() method for lists, see below
            # sorts it from largest to lowest
            sorted_list = sorted(total_appear_time_list, reverse=True) '''

            # makes the count back to zero for the amount of words in the dna file
            '''total_appear_times = 0 '''

        # makes another list to store the biggest number of times the dna string has appeared
        ''' dna_repeated_list.append(sorted_list[0]) '''
        dna_repeated_list.append(max(total_appear_time_list))

        # it sets the list of all the times the dna pattern has been found
        ''' total_appear_time_list = [] '''

    return dna_repeated_list


dna_repeated_list = get_repeat_list(letters=letters)


def get_match(lst=[], dna_repeated_list=[]):

    # loop through the dna file with the people on it checking all the verticle rows except the first
    for m in range(len(lst) - 1):
        adding = 0
        m = m + 1
        # loop through the dna file with the people on it to checking the numbers but doesn't check the names
        for q in range(len(lst[1]) - 1):
            q = q + 1  # makes the variable q start at 1
            lst[m][q] = int(lst[m][q])  # makes it an int to compare it
            # compares the double list to the singular list with all the maximumun number of times the pattern appears in a row
            if lst[m][q] != dna_repeated_list[q - 1]:
                adding += 1  # if it does not match then add it by one
        if adding == 0:  # if it all matches then print the name of the person
            print(f"{lst[m][0]}")
            exit(1)
        # adding = 0  # makes the variable adding go back to zero

    print(f"No match")  # if it has not been found


get_match(lst=lst, dna_repeated_list=dna_repeated_list)
