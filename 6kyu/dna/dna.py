from sys import argv, exit
import csv


def main():

    # check_args(argument=argv)

    # dna_dict, people_list = get_people(peoplefile=argv[1])
    dna_dict, people_list = get_people(peoplefile='./databases/large.csv')
    dna_string = get_dna_string(dnafile='./sequences/5.txt').rstrip()
    # dna_string = get_dna_string(dnafile=argv[2]).rstrip()
    totals = calc_STR(dna_string=dna_string, str_list=dna_dict['SRTs'])
    string_numbers = make_strings(totals)
    print(dna_match(people=people_list, numbers=string_numbers))

    # print(dna_match(people=people_list, numbers=totals))
    # print(dna_string.rstrip())
    # print(dna_list)
    # print(people_list)


def check_args(argument=[]):
    ''' incorrect len(argv) -> print error '''
    if len(argument) != 3:
        print('Please include the correct number of files')
        exit(1)


def get_people(peoplefile=''):
    ''' first CLA -> CSV file open CSV and read contents into memory first row
    will be column names starting with 'name' and followed by str sequences '''
    with open(peoplefile, newline='') as f:
        fieldnames = ['name']
        seq_reader = csv.DictReader(f, fieldnames=fieldnames, restkey='SRTs')
        CSV = {}
        for index, row in enumerate(seq_reader):
            if index == 0:
                dna_list = row
            else:
                # print(row['name'], row['SRTs'])
                CSV[row['name']] = row['SRTs']
        return dna_list, CSV


def get_dna_string(dnafile=''):
    '''second CLA -> text file of DNA sequence open DNA file and read contents into memory'''
    with open(dnafile, newline='') as dnaf:
        dna_string = dnaf.read()
        return dna_string


def calc_STR(dna_string='', str_list=[]):
    ''' compute longest run of eact STR in DNA '''
    count = [0 for i in str_list]
    # print(str_list)
    # print(count)
    for index, STR in enumerate(str_list):
        length = len(STR)
        for i, v in enumerate(dna_string):
            if v == STR[0]:
                count[index] += is_match(STR=STR,
                                         dna_string=dna_string[i:i+length])
    return count


def is_match(STR='', dna_string=''):
    ''' check if seq matces STR, return 1 if true else 0 '''
    ret = 1 if STR == dna_string else 0
    return ret


def make_strings(number_list=[]):
    return [str(i) for i in number_list]


def dna_match(people={}, numbers=[]):
    # print(people)

    for person in people:
        # print(f"person is {person}\nnumbers is {numbers}")
        # print(f"person's srts are {people[person]}\n")
        if people[person] == numbers:
            return person
    return 'No match'


# if count(STR) == person from CSV -> print person.name
# if no match print 'No match'
if __name__ == '__main__':
    main()
