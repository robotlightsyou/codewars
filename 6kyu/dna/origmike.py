import sys
if len(sys.argv) != 3:  # asks for a valid input
    print(f"Usage: python dna.py data.csv sequence.txt")
    exit(1)

# defines all the variables
document_file = sys.argv[1] 
dna_file = sys.argv[2]
text = open(dna_file)
people = open(document_file)
dna_list = []
letters = []
total_appear_time_list = []
temp_list = []
list_of_people = []
list = []
dna_repeated_list = []
total_appear_times = 0
adding = 0
word = ''
peoples_dna = ''

for words in text:  # makes a list of all the dna letters in the letters file
    for letter in words:
        letters.append(letter)


for line in people:  # adds all of the sentences into a list
    dna_list.append(line)

for i in range(len(dna_list)):  # makes the dna_list into a string
    peoples_dna += dna_list[i]
peoples_dna = peoples_dna.strip()

for sentence in peoples_dna.splitlines():  # makes a double list where there is few list in a list
    list.append(sentence.split(','))

for m in range(len(list[0]) - 1):
    m = m + 1
    for i in range(len(letters) - 3):  # checks the number of times something appeared in the list

        word = ""  # makes it go be nothing

        try:  # if it gets to the end of the dna line it will make a list of range not found
            for a in range(len(list[0][m])):

                word += letters[a + i]
        except:
            break
        while word == list[0][m]:  # does it until the word is not the dna part

            total_appear_times += 1

            word = ''

            try:
                i = i + len(list[0][m])

                for a in range(len(list[0][m])):

                    word += letters[a + i]

            except:  # remember to check if there is a error 'list index out of range'
                break  # exits the loop becuase it is at the end of the dna line
        total_appear_time_list.append(total_appear_times)  # makes the number of repetion into a list
        sorted_list = sorted(total_appear_time_list, reverse=True)  # sorts it from largest to lowest
        total_appear_times = 0  # makes the count back to zero for the amount of words in the dna file
    dna_repeated_list.append(sorted_list[0])  # makes another list to store the biggest number of times the dna string has appeared
    total_appear_time_list = []  # it sets the list of all the times the dna pattern has been found

for m in range(len(list) - 1):  # loop through the dna file with the people on it checking all the verticle rows except the first
    m = m + 1
    for q in range(len(list[1]) - 1):  # loop through the dna file with the people on it to checking the numbers but doesn't check the names
        q = q + 1  # makes the variable q start at 1
        list[m][q] = int(list[m][q])  # makes it an int to compare it
        if list[m][q] != dna_repeated_list[q - 1]:  # compares the double list to the singular list with all the maximumun number of times the pattern appears in a row
            adding += 1  # if it does not match then add it by one
    if adding == 0:  # if it all matches then print the name of the person
        print(f"{list[m][0]}")
        exit(1)
    adding = 0  # makes the variable adding go back to zero

print(f"No match")  # if it has not been found
