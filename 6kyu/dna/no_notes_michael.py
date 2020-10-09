from sys import argv


def main():
    check_args(argument=argv)
    letters = get_letters()
    lst = get_dna()
    dna_repeated_list = get_repeat_list(letters=letters, lst=lst)
    get_match(lst=lst, dna_repeated_list=dna_repeated_list)


def check_args(argument=[]):
    ''' checks argv to confirm proper input from user '''
    if len(argv) != 3:  # asks for a valid input
        print(f"Usage: python dna.py data.csv sequence.txt")
        exit(1)


def get_letters():
    ''' reads in DNA sequence from .txt file '''
    with open(argv[2], newline='') as f:
        text = f.read()
    letters = [letter for word in text for letter in word]
    return letters


def get_dna():
    ''' reads in people/SRT counts from .csv file'''
    with open(argv[1], newline='') as f:
        people = f.read()
    dna_list = [line for line in people]

    peoples_dna = ''.join([val for _, val in enumerate(dna_list)]).strip()
    lst = [sentence.split(',') for sentence in peoples_dna.splitlines()]
    return lst


'''    peoples_dna = ''
    for _, val in enumerate(dna_list):  # makes the dna_list into a string
        peoples_dna += val
    peoples_dna = peoples_dna.strip() '''


def get_repeat_list(letters=[], lst=[]):
    ''' determines longest count of repeating DNA sequences '''
    dna_repeated_list = []

    for m in range(len(lst[0]) - 1):
        total_appear_time_list = []
        m = m + 1

        # checks the number of times something appeared in the list
        for i in range(len(letters) - 3):
            total_appear_times = 0
            word = ""  # makes it go be nothing

            try:  # if it gets to the end of the dna line it will make a list of range not found
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

        # makes another list to store the biggest number of times the dna string has appeared
        dna_repeated_list.append(max(total_appear_time_list))

    return dna_repeated_list


def get_match(lst=[], dna_repeated_list=[]):
    ''' checks lists of DNA counts against people list '''
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

    print(f"No match")  # if it has not been found


if __name__ == '__main__':
    main()
